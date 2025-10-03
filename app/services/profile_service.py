from app.api.models.user_profile import UserProfile
from app.api.models.create_user_profile_request import CreateUserProfileRequest
from app.api.models.update_user_profile_request import UpdateUserProfileRequest
from app.repository.profile_repository import UserProfilesRepository
import uuid
from app.schemas.user_profile_table import UserProfilesTable
from app.exception import MandatoryFieldMissingError,ProfileNotFoundException

class ProfileService:
    def get_profiles():
        return UserProfilesRepository.get_all_profiles()

    def get_profiles_by_id(id:str):
        return UserProfilesRepository.get_profile_by_id(id)

    def update_profile(id:str, profile :UpdateUserProfileRequest):
        db_profile = UserProfilesRepository.get_profile_by_id(id)
        if not db_profile:
            raise ProfileNotFoundException(id)
        if profile.displayName is not None:
            db_profile.display_name = profile.displayName
        if profile.avatarUrl is not None:
            db_profile.avatar_url = profile.avatarUrl
        if profile.statusMessage is not None:
            db_profile.status_message = profile.statusMessage
        return UserProfilesRepository.update_profile(db_profile)
       

    def create_profiles(profile: CreateUserProfileRequest):
        if not profile.username:
            raise MandatoryFieldMissingError("username")

        db_profile = UserProfilesTable(
                id=str(uuid.uuid4()),
                username=profile.username,
                display_name=profile.displayName,
                avatar_url=profile.avatarUrl,
                status_message=profile.statusMessage,
            )
        return UserProfilesRepository.create_profile(db_profile)

    def delete_profiles():
        return UserProfilesRepository.delete_profile(id)