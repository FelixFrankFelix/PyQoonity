from pydantic import BaseModel
from typing import Union,List
from model.request.CrudRequest import User

class BaseResponse(BaseModel):
    responseCode: str
    responseMessage: str
    

class DetailedResponseUser(BaseModel):
    responseCode: str
    responseMessage: str
    body: User

class DetailedResponseUsers(BaseModel):
    responseCode: str
    responseMessage: str
    body: List[User]
  
ResponseUnionUser = Union[DetailedResponseUser, BaseResponse]
ResponseUnionUsers = Union[DetailedResponseUsers, BaseResponse]