from pydantic import BaseModel
from typing import Optional
class CreateUserProfileRequest(BaseModel):
    username: str
    displayName: str
    avatarUrl: Optional[str] = None
    StatusMessage: Optional[str]= None
    avatarUrl: Optional[str]= None
    createdAt: Optional[str]= None
    updatedAt: Optional[str]= None