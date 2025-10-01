
from fastapi import APIRouter, HTTPException, status
from typing import List
from app.api.models.user_profile import UserProfile
from app.api.models.create_user_profile_request import CreateUserProfileRequest
from app.api.models.update_user_profile_request import UpdateUserProfileRequest
from app.services.profile_service import ProfileService

router = APIRouter()


@router.get("/profiles",response_model= List[UserProfile])
def get_profiles():
    return ProfileService.get_profiles()

@router.post("/profiles", response_model=UserProfile,status_code=201)
def create_profile(profile: CreateUserProfileRequest):
    created = ProfileService.create_profiles(profile)
    if not created:
        raise HTTPException(status_code=409, detail="Username already exists")
    return UserProfile.model_validate(created)

@router.get("/profiles/{id}",response_model=UserProfile)
def get_profile_by_id(id:str):
    result = ProfileService.get_profiles_by_id(id)
    if not result:
        raise HTTPException(status_code=404, detail="Profile not found")
    return UserProfile.model_validate(result)

@router.put("/profiles/{id}",response_model=UserProfile)
def update_profile(id:str, profile :UpdateUserProfileRequest):
    updated = ProfileService.update_profile(id, profile)
    if not updated:
        raise HTTPException(status_code=404, detail="Profile not found")
    return UserProfile.model_validate(updated)
@router.delete("/profiles/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_profile(id:str):
    deleted = ProfileService.delete_profiles(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Profile not found")
    return None

