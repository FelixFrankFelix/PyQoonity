from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List,Union
import crud, schemas
from db import SessionLocal, engine
from utility.exceptions import ResponseConstant

app = FastAPI()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create-user/", response_model=schemas.ResponseUnionUser)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.user_email)
    if db_user:
        return {
        "responseCode": ResponseConstant.DUPLICATE_RECORD.responseCode,
        "responseMessage": "email already exist", 
        }
    return {
        "responseCode": ResponseConstant.SUCCESS.responseCode,
        "responseMessage": ResponseConstant.SUCCESS.responseMessage, 
        "body" : crud.create_user(db=db, user=user)
        }

@app.get("/read-users/", response_model= schemas.ResponseUnionUsers)
def read_users(db: Session = Depends(get_db)):
    return {
        "responseCode": ResponseConstant.SUCCESS.responseCode,
        "responseMessage": ResponseConstant.SUCCESS.responseMessage, 
        "body" : crud.get_users(db)
        }


@app.get("/read-user-by-id/{user_id}", response_model=schemas.ResponseUnionUser)
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        return ResponseConstant.NO_SUCH_ISSUER
    return {
        "responseCode": ResponseConstant.SUCCESS.responseCode,
        "responseMessage": ResponseConstant.SUCCESS.responseMessage, 
        "body" : db_user
        }

@app.get("/read-user-by-email/{user_email}", response_model=schemas.ResponseUnionUser)
def read_user_by_email(user_email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user_email=user_email)
    if db_user is None:
        return ResponseConstant.NO_SUCH_ISSUER
    return {
        "responseCode": ResponseConstant.SUCCESS.responseCode,
        "responseMessage": ResponseConstant.SUCCESS.responseMessage, 
        "body" : db_user
        }

@app.get("/read-user-by-name/{user_name}", response_model=schemas.ResponseUnionUsers)
def read_user_by_name(user_name: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, user_name=user_name)
    if not db_user:
        return ResponseConstant.NO_SUCH_ISSUER
    return {
        "responseCode": ResponseConstant.SUCCESS.responseCode,
        "responseMessage": ResponseConstant.SUCCESS.responseMessage, 
        "body" : db_user
        }
        


@app.post("/update-user/{user_id}", response_model=schemas.ResponseUnionUser)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        return ResponseConstant.NO_SUCH_ISSUER
    return {
        "responseCode": ResponseConstant.SUCCESS.responseCode,
        "responseMessage": ResponseConstant.SUCCESS.responseMessage, 
        "body" : crud.update_user(db=db, user_id=user_id, user=user)
        }



@app.post("/delete-user/{user_id}", response_model=schemas.ResponseUnionUser)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        return ResponseConstant.NO_SUCH_ISSUER
    return {
        "responseCode": ResponseConstant.SUCCESS.responseCode,
        "responseMessage": ResponseConstant.SUCCESS.responseMessage, 
        "body" : crud.delete_user(db=db, user_id=user_id)
        }
