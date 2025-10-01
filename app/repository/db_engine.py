from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Align with docker-compose (MYSQL_DATABASE: Chatapp_Db)
DATABASE_URL = "mysql+pymysql://root:Pass123@localhost:3307/Chatapp_Db"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()