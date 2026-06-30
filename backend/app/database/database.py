from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL="postgresql://sentinelx:SentinelX2026!@postgres:5432/sentinelx"

engine=create_engine(DATABASE_URL)

SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
