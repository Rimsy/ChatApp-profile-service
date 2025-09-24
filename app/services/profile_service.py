from app.api.models.user_profile import UserProfile
from app.api.models.create_user_profile_request import CreateUserProfileRequest
from app.api.models.update_user_profile_request import UpdateUserProfileRequest


class ProfileService:
    def get_profiles():
        return [
        {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "username": "john_doe",
            "displayName": "John Doe",
            "avatarUrl": "https://example.com/avatar.jpg",
            "statusMessage": "Hello, world!",
            "createdAt": "2023-09-24T12:00:00Z",
            "updatedAt": "2023-09-24T12:00:00Z"
        }
    ]

    def get_profiles_by_id(id:str):
        if id !="123e4567-e89b-12d3-a456-426614174000":
            raise HTTPException(status_code=404, detail="Resource not found")
        return{
            "id": id,
            "username": "john_doe",
            "displayName": "John Doe",
            "avatarUrl": "https://example.com/avatar.jpg",
            "statusMessage": "Hello, world!",
            "createdAt": "2023-09-24T12:00:00Z",
            "updatedAt": "2023-09-24T12:00:00Z"
        }

    def update_profile(id:str, profile :UpdateUserProfileRequest):
        return {
            "id": id,
            "username": "john_doe",
            "displayName": profile.displayName or "John Doe",
            "avatarUrl": profile.avatarUrl or "https://example.com/avatar.jpg",
            "statusMessage": profile.statusMessage or "Hello, world!",
            "createdAt": "2023-09-24T12:00:00Z",
            "updatedAt": "2023-09-24T13:00:00Z"
        }
       

    def create_profiles(profile: CreateUserProfileRequest):
         return{
            "id": "223e4567-e89b-12d3-a456-426614174001",
            "username": profile.username,
            "displayName": profile.displayName,
            "avatarUrl": profile.avatarUrl,
            "statusMessage": profile.statusMessage,
            "createdAt": "2023-09-24T12:00:00Z",
            "updatedAt": "2023-09-24T12:00:00Z"
        }

    def delete_profiles():
        pass