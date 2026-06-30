from app.database.database import engine
from app.database.base import Base

import app.models.user
import app.models.session
import app.models.security_event

Base.metadata.create_all(bind=engine)

print("Database initialized")
