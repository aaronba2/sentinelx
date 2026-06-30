from sqlalchemy import Column,Integer,String,DateTime
from datetime import datetime
from app.database.base import Base

class SecurityEvent(Base):
    __tablename__="security_events"

    id=Column(Integer,primary_key=True,index=True)
    event=Column(String)
    ip=Column(String)
    username=Column(String)
    severity=Column(String)
    created_at=Column(DateTime,default=datetime.utcnow)
