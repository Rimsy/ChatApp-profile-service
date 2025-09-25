from app.api.models.user_profile import UserProfile
from app.api.models.create_user_profile_request import CreateUserProfileRequest
from app.api.models.update_user_profile_request import UpdateUserProfileRequest
from app.repository.profile_repository import UserProfilesRepository

class ProfileService:
    def get_profiles():
        return UserProfilesRepository.get_all_profiles()

    def get_profiles_by_id(id:str):
        return UserProfilesRepository.get_profile_by_id(id)

    def update_profile(id:str, profile :UpdateUserProfileRequest):
        return UserProfilesRepository.update_profile(id)
       

    def create_profiles(profile: CreateUserProfileRequest):
         return UserProfilesRepository.create_profile()

    def delete_profiles():
        return UserProfilesRepository.delete_profile(id)