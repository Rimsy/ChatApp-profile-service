from fastapi import FastAPI,HTTPException,status
from fastapi.responses import JSONResponse
from fastapi.requests import Request

class MandatoryFieldMissingError(HTTPException):
    def __init__(self, field_name:str):
        detail = f"The field '{field_name}' is missing"
        super().__init__(status_code = status.HTTP_422_UNPROCESSABLE_CONTENT, detail= detail)

class ProfileNotFoundException(HTTPException):
    def __init__(self, profile_id:str):
        detail = f"Profile with the given id - '{profile_id}' doesn't exist"
        super().__init__(status_code = status.HTTP_404_NOT_FOUND,detail= detail)

class DuplicateUserNameException(HTTPException):
    def __init__(self, username:str):
        detail = f"Username '{username}' already exists"
        super().__init__(status_code= status.HTTP_409_CONFLICT,detail = detail)
