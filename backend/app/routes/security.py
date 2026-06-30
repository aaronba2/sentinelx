from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.security_service import log_event

router = APIRouter(prefix="/security", tags=["Security"])

@router.post("/event")
def create_event(db: Session = Depends(get_db)):
    event = log_event(
        db=db,
        event="LOGIN_SUCCESS",
        ip="127.0.0.1",
        username="demo",
        severity="LOW"
    )

    return {
        "id": event.id,
        "status": "stored"
    }
