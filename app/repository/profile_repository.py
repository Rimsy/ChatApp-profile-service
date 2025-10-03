from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.schemas.user_profile_table import UserProfilesTable
from app.api.models.create_user_profile_request import CreateUserProfileRequest
from app.api.models.update_user_profile_request import UpdateUserProfileRequest
import uuid
from app.repository.db_engine import SessionLocal
from app.exception import (
    ProfileNotFoundException,
    DuplicateUserNameException,
)

class UserProfilesRepository:
    def create_profile(profile:UserProfilesTable):
        
        db: Session = SessionLocal()
        try:
            existing_user = db.query(UserProfilesTable).filter(UserProfilesTable.username == profile.username).first()
            if existing_user:
                raise DuplicateUserNameException(profile.username)
            db.add(profile)
            db.commit()
            db.refresh(profile)
            return profile
        except IntegrityError:
            db.rollback()
            raise
        finally:
            db.close()

    def get_all_profiles():
        db: Session = SessionLocal()
        try:
            return db.query(UserProfilesTable).all()
        finally:
            db.close()

    def get_profile_by_id(profile_id: str):
        db: Session = SessionLocal()
        try:
            profile = db.query(UserProfilesTable).filter(UserProfilesTable.id == profile_id).first()
            if not profile:
                raise ProfileNotFoundException(profile_id)
            return profile
        finally:
            db.close()

    def update_profile(profile: UserProfilesTable):
        db: Session = SessionLocal()
        try:
            db.commit()
            db.refresh(profile)
            return profile
        finally:
            db.close()

    def delete_profile(profile_id: str):
        db: Session = SessionLocal()
        try:
            db_profile = db.query(UserProfilesTable).filter(UserProfilesTable.id == profile_id).first()
            if not db_profile:
                raise ProfileNotFoundException(profile_id)
            db.delete(db_profile)
            db.commit()
            return db_profile
        finally:
            db.close()
