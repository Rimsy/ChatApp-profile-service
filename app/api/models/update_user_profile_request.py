from pydantic import BaseModel
from typing import Optional

class UpdateUserProfileRequest(BaseModel):
    displayName: Optional[str] = None
    avatarUrl: Optional[str] = None
    statusMessage: Optional[str] = None