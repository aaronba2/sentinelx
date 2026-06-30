from sqlalchemy.orm import Session
from app.models.session import Session as UserSession

def create_session(db,username,ip,user_agent,token):

    session=UserSession(
        username=username,
        ip=ip,
        user_agent=user_agent,
        token=token
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    return session

def count_sessions(db,username):

    return db.query(UserSession).filter(
        UserSession.username==username
    ).count()
