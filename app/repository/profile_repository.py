from sqlalchemy.orm import Session
from app.schemas.user_profile_table import UserProfilesTable
from app.api.models.create_user_profile_request import CreateUserProfileRequest
from app.api.models.update_user_profile_request import UpdateUserProfileRequest
import uuid
from app.repository import db_engine

class UserProfilesRepository:
    def __init__(self):
        self.db = db_engine.get_db()

    def create_profile(self, profile: CreateUserProfileRequest):
        db_profile = UserProfilesTable(
            id=str(uuid.uuid4()),
            username=profile.username,
            display_name=profile.displayName,
            avatar_url=profile.avatarUrl,
            status_message=profile.statusMessage
        )
        self.db.add(db_profile)
        self.db.commit()
        self.db.refresh(db_profile)
        return db_profile

    def get_all_profiles(self):
        return self.db.query(UserProfilesTable).all()

    def get_profile_by_id(self, profile_id: str):
        return self.db.query(UserProfilesTable).filter(UserProfilesTable.id == profile_id).first()

    def update_profile(self, profile_id: str, profile: UpdateUserProfileRequest):
        db_profile = self.db.query(UserProfilesTable).filter(UserProfilesTable.id == profile_id).first()
        if not db_profile:
            return None
        if profile.displayName is not None:
            db_profile.display_name = profile.displayName
        if profile.avatarUrl is not None:
            db_profile.avatar_url = profile.avatarUrl
        if profile.statusMessage is not None:
            db_profile.status_message = profile.statusMessage
        self.db.commit()
        self.db.refresh(db_profile)
        return db_profile

    def delete_profile(self, profile_id: str):
        db_profile = self.db.query(UserProfilesTable).filter(UserProfilesTable.id == profile_id).first()
        if not db_profile:
            return None
        self.db.delete(db_profile)
        self.db.commit()
        return db_profile
