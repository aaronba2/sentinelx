from sqlalchemy import Column,Integer,String,DateTime
from datetime import datetime
from app.database.base import Base

class Session(Base):
    __tablename__="sessions"

    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,index=True)
    ip=Column(String)
    user_agent=Column(String)
    token=Column(String)
    created_at=Column(DateTime,default=datetime.utcnow)
