
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
    return ProfileService.update_profiles()

@router.get("/profiles/{id}",response_model=UserProfile)
def get_profile_by_id(id:str):
    return ProfileService.get_profiles_by_id()

@router.put("/profiles/{id}",response_model=UserProfile)
def update_profile(id:str, profile :UpdateUserProfileRequest):
    return ProfileService.update_profile
@router.delete("/profiles/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_profile(id:str):
    
    return

