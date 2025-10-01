from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.schemas.user_profile_table import UserProfilesTable
from app.api.models.create_user_profile_request import CreateUserProfileRequest
from app.api.models.update_user_profile_request import UpdateUserProfileRequest
import uuid
from app.repository.db_engine import SessionLocal


class UserProfilesRepository:
    def create_profile(self, profile: CreateUserProfileRequest):
        db: Session = SessionLocal()
        try:
            db_profile = UserProfilesTable(
                id=str(uuid.uuid4()),
                username=profile.username,
                display_name=profile.displayName,
                avatar_url=profile.avatarUrl,
                status_message=profile.statusMessage,
            )
            db.add(db_profile)
            db.commit()
            db.refresh(db_profile)
            return db_profile
        except IntegrityError:
            db.rollback()
            return None
        finally:
            db.close()

    def get_all_profiles(self):
        db: Session = SessionLocal()
        try:
            return db.query(UserProfilesTable).all()
        finally:
            db.close()

    def get_profile_by_id(self, profile_id: str):
        db: Session = SessionLocal()
        try:
            return db.query(UserProfilesTable).filter(UserProfilesTable.id == profile_id).first()
        finally:
            db.close()

    def update_profile(self, profile_id: str, profile: UpdateUserProfileRequest):
        db: Session = SessionLocal()
        try:
            db_profile = db.query(UserProfilesTable).filter(UserProfilesTable.id == profile_id).first()
            if not db_profile:
                return None
            if profile.displayName is not None:
                db_profile.display_name = profile.displayName
            if profile.avatarUrl is not None:
                db_profile.avatar_url = profile.avatarUrl
            if profile.statusMessage is not None:
                db_profile.status_message = profile.statusMessage
            db.commit()
            db.refresh(db_profile)
            return db_profile
        finally:
            db.close()

    def delete_profile(self, profile_id: str):
        db: Session = SessionLocal()
        try:
            db_profile = db.query(UserProfilesTable).filter(UserProfilesTable.id == profile_id).first()
            if not db_profile:
                return None
            db.delete(db_profile)
            db.commit()
            return db_profile
        finally:
            db.close()
