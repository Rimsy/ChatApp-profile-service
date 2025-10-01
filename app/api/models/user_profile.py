from pydantic import BaseModel, Field
from pydantic import ConfigDict
from typing import Optional
from datetime import datetime

class UserProfile(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    id: Optional[str] = None
    username: str
    displayName: str = Field(serialization_alias="displayName", validation_alias="display_name")
    avatarUrl: Optional[str] = Field(default=None, serialization_alias="avatarUrl", validation_alias="avatar_url")
    statusMessage: Optional[str] = Field(default=None, serialization_alias="statusMessage", validation_alias="status_message")
    createdAt: Optional[datetime] = Field(default=None, serialization_alias="createdAt", validation_alias="created_at")
    updatedAt: Optional[datetime] = Field(default=None, serialization_alias="updatedAt", validation_alias="updated_at")