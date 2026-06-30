from sqlalchemy import Column,Integer,String,Boolean
from app.database.base import Base

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True)
    password=Column(String)
    role=Column(String,default="user")
    active=Column(Boolean,default=True)
