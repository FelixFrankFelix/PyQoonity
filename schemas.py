from pydantic import BaseModel,Field,StrictStr,field_validator
from typing import Optional,Any,Dict,Union
from datetime import datetime

class UserBase(BaseModel):
    user_name: str
    user_email: str

class UserCreate(BaseModel):
    user_name: StrictStr
    user_email: StrictStr
    user_password: StrictStr

    @field_validator('user_name', 'user_email', 'user_password')
    def not_empty(cls, v):
        if v.strip() == "":
            raise ValueError('must not be an empty string')
        return v

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


class BaseResponse(BaseModel):
    ResponseCode: str
    ResponseMessage: str

class DetailedResponse(BaseModel):
    ResponseCode: str
    ResponseMessage: str
    body: User


    

ResponseUnion = Union[DetailedResponse, BaseResponse]