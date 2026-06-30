from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.password import hash_password

def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, username: str, password: str):

    user = User(
        username=username,
        password=hash_password(password),
        role="user",
        active=True
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
