from fastapi import FastAPI

from app.routes.health import router as health_router
from app.routes.auth import router as auth_router
from app.routes.security import router as security_router

app = FastAPI(
    title="SentinelX",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(security_router)

@app.get("/")
def root():
    return {"message": "SentinelX API Online"}
