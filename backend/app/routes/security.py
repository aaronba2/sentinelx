from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.security import SecurityEventRequest
from app.services.security_service import log_event

router = APIRouter(prefix="/security", tags=["Security"])


@router.post("/event")
def create_event(
    payload: SecurityEventRequest,
    request: Request,
    db: Session = Depends(get_db),
):
    client_ip = payload.ip
    if client_ip == "unknown" and request.client:
        client_ip = request.client.host

    event = log_event(
        db=db,
        event=payload.resolved_event(),
        ip=client_ip,
        username=payload.username,
        severity=payload.severity,
    )

    return {
        "id": event.id,
        "status": "stored",
        "event": event.event,
        "ip": event.ip,
        "username": event.username,
        "severity": event.severity,
        "metadata": payload.metadata or {},
    }
