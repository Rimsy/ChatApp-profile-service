from pydantic import BaseModel
from typing import Optional

class Error(BaseModel):
    code:int
    message:str