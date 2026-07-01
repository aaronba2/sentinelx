from pydantic import BaseModel, Field


class SecurityEventRequest(BaseModel):
    event: str | None = None
    type: str | None = None
    ip: str = "unknown"
    username: str = "unknown"
    severity: str = Field(default="LOW", pattern="^(LOW|MEDIUM|HIGH)$")
    metadata: dict | None = None

    def resolved_event(self) -> str:
        return (self.event or self.type or "UNKNOWN").strip()
