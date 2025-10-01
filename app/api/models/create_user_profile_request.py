from pydantic import BaseModel
from typing import Optional
class CreateUserProfileRequest(BaseModel):
    username: str
    displayName: str
    avatarUrl: Optional[str] = None
    statusMessage: Optional[str] = None