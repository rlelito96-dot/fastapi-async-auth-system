from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    website: str
    age: int
    role: str

class UserCreate(User):
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    website: Optional[str] = None
    age: Optional[int] = None
    role: Optional[str] = None

class UserOut(User):
    id: int

    model_config = {
        "from_attributes": True

    }

class Token(BaseModel):
    access_token: str
    token_type: str