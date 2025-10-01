from fastapi import FastAPI
from app.api.profile_route import router as profile_router
from app.repository.db_engine import engine
from app.schemas.user_profile_table import Base

app = FastAPI()


app.include_router(profile_router)

# Create tables on startup if they don't exist
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)