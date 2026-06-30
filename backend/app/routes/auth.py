from app.security.bruteforce import (
    is_blocked,
    login_failed,
    login_success
)

from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from app.schemas.login import LoginRequest
from app.schemas.user import UserCreate

from app.database.database import get_db

from app.utils.token import create_access_token
from app.utils.password import verify_password

from app.services.user_service import create_user, get_user
from app.services.session_service import create_session
from app.services.security_service import log_event

from app.security.user_agent import suspicious_agent
from app.security.multi_login import detect_multiple_sessions
from app.security.rate_limit import allow
from app.security.risk_score import compute_score

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    if get_user(db, user.username):
        return {
            "status": "ERROR",
            "message": "User already exists"
        }

    create_user(db, user.username, user.password)

    return {
        "status": "OK",
        "message": "User created"
    }


@router.post("/login")
def login(
    data: LoginRequest,
    request: Request,
    db: Session = Depends(get_db)
):

    ip = request.client.host

    # Blocage anti brute-force
    if is_blocked(ip):

        log_event(
            db,
            "BRUTE_FORCE_BLOCK",
            ip,
            data.username,
            "HIGH"
        )

        return {
            "status": "BLOCK",
            "reason": "IP temporarily blocked"
        }

    user = get_user(db, data.username)

    if user is None:

        login_failed(ip)

        return {
            "status": "ERROR",
            "message": "Invalid username or password"
        }

    if not verify_password(data.password, user.password):

        login_failed(ip)

        log_event(
            db,
            "LOGIN_FAILED",
            ip,
            data.username,
            "MEDIUM"
        )

        return {
            "status": "ERROR",
            "message": "Invalid username or password"
        }

    # Login réussi
    login_success(ip)

    user_agent = request.headers.get("User-Agent", "Unknown")

    if not allow(ip):

        log_event(
            db,
            "RATE_LIMIT",
            ip,
            data.username,
            "HIGH"
        )

        return {
            "status": "BLOCK",
            "reason": "Too many requests"
        }

    token = create_access_token(
        {
            "username": data.username
        }
    )

    create_session(
        db,
        data.username,
        ip,
        user_agent,
        token
    )

    multi = detect_multiple_sessions(
        db,
        data.username
    )

    bad_agent = suspicious_agent(
        user_agent
    )

    score = compute_score(
        multi_login=multi,
        bad_agent=bad_agent
    )

    severity = "LOW"

    if score >= 25:
        severity = "MEDIUM"

    if score >= 50:
        severity = "HIGH"

    log_event(
        db,
        "LOGIN",
        ip,
        data.username,
        severity
    )

    return {
        "status": "ALLOW",
        "token": token,
        "risk_score": score,
        "multiple_sessions": multi,
        "bad_user_agent": bad_agent
    }
