from fastapi import FastAPI
from app.api.profile_route import router as profile_router

app = FastAPI()


app.include_router(profile_router)