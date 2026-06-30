from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY="CHANGE_ME_2026"
ALGORITHM="HS256"

def create_access_token(data: dict):
    payload=data.copy()
    payload["exp"]=datetime.utcnow()+timedelta(hours=24)
    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
