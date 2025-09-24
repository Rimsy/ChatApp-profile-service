from pydantic import BaseModel
from typing import Optional

class UserProfile(BaseModel):
    id:Optional[str] = None
    username : str
    displayName : str
    avatarUrl:Optional[str]= None
    statusMessage : Optional[str]=None
    createdAt: Optional[str]= None
    updatedAt: Optional[str]= None