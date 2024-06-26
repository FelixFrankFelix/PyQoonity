from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    user_name: str
    user_email: str

class UserCreate(UserBase):
    user_password: str


class UserUpdate(BaseModel):
    user_name: Optional[str] = None
    user_email: Optional[str] = None
    user_password: Optional[str] = None
    user_status: Optional[str] = None

class User(UserBase):
    user_id: int
    user_created_at: datetime
    user_updated_at: datetime
    user_status: str

    class Config:
        orm_mode = True
