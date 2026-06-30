from sqlalchemy.orm import Session
from app.models.security_event import SecurityEvent

def log_event(db: Session, event: str, ip: str, username: str, severity: str):
    security_event = SecurityEvent(
        event=event,
        ip=ip,
        username=username,
        severity=severity
    )
    db.add(security_event)
    db.commit()
    db.refresh(security_event)
    return security_event
