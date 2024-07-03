from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List,Union
from model.request import CrudRequest
from model.response import CrudResponse
from repository.database import CrudRepository
from db import SessionLocal, engine
from utility.exceptions import ResponseConstant
from service import CrudService

app = FastAPI()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create-user/", response_model=CrudResponse.ResponseUnionUser)
def create_user_controller(user: CrudRequest.UserCreate, db: Session = Depends(get_db)):
    db_user = CrudRepository.get_user_by_email(db, user.user_email)
    if not db_user:
        db_user = CrudRepository.create_user(db=db, user=user)
        return CrudService.create_user_service(db_user)
    return CrudService.create_user_service(None)

@app.get("/read-users/", response_model= CrudResponse.ResponseUnionUsers)
def read_users_controller(db: Session = Depends(get_db)):
    db_user = CrudRepository.get_users(db)
    return CrudService.read_users_service(db_user)


@app.get("/read-user-by-id/{user_id}", response_model=CrudResponse.ResponseUnionUser)
def read_user_by_id_controller(user_id: int, db: Session = Depends(get_db)):
    db_user = CrudRepository.get_user_by_id(db, user_id=user_id)
    return CrudService.read_user_by_id_service(db_user)

@app.get("/read-user-by-email/{user_email}", response_model=CrudResponse.ResponseUnionUser)
def read_user_by_email_controller(user_email: str, db: Session = Depends(get_db)):
    db_user = CrudRepository.get_user_by_email(db, user_email=user_email)
    return CrudService.read_user_by_email_service(db_user)

@app.get("/read-user-by-name/{user_name}", response_model=CrudResponse.ResponseUnionUsers)
def read_user_by_name(user_name: str, db: Session = Depends(get_db)):
    db_user = CrudRepository.get_user_by_name(db, user_name=user_name)
    return CrudService.read_user_by_name_service(db_user)


@app.post("/update-user/{user_id}", response_model=CrudResponse.ResponseUnionUser)
def udate_user_controller(user_id: int, user: CrudRequest.UserUpdate, db: Session = Depends(get_db)):
    db_user = CrudRepository.get_user_by_id(db, user_id=user_id)
    return CrudService.update_user_service(db_user)


@app.post("/delete-user/{user_id}", response_model=CrudResponse.ResponseUnionUser)
def delete_user_controller(user_id: int, db: Session = Depends(get_db)):
    db_user = CrudRepository.get_user_by_id(db, user_id=user_id)
    return CrudService.delete_user_service(db_user)