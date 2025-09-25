# // have db models here

# table name is user_profiles 
#  model name is
from sqlalchemy import Column,String,DateTime,func
from sqlalchemy.dialects.mysql import CHAR,VARCHAR
from sqlalchemy.ext.declarative import declarative_base
import uuid
Base = declarative_base()
class UserProfilesTable(Base):
    __tablename__ = "user_profiles"
    id = Column(CHAR(36), primary_key =True,default=lambda: str(uuid.uuid4()),nullable=False)
    username = Column(VARCHAR(50),unique=True,nullable=False,index=True)
    display_name = Column(VARCHAR(100),nullable=False)
    avatar_url = Column(VARCHAR(255))
    status_message = Column(VARCHAR(255))
    created_at = Column(DateTime,nullable=False,server_default=func.now())
    updated_at = Column(DateTime,nullable=False,server_default=func.now(),onupdate=func.now())
