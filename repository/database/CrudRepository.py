from sqlalchemy.orm import Session
from sqlalchemy import text
from datetime import datetime
from model.request.CrudRequest import UserCreate, UserUpdate
from typing import List
from fastapi import HTTPException
from repository.database.query import CrudQuery

def get_user_by_id(db: Session, user_id: int):
    result = db.execute(text(CrudQuery.READ_BY_ID), 
                        {'user_id': user_id})
    return result.fetchone()

def get_user_by_email(db: Session, user_email: str):
    result = db.execute(text(CrudQuery.READ_BY_EMAIL), 
                        {'user_email': user_email})
    return result.fetchone()

def get_user_by_name(db: Session, user_name: str):
    result = db.execute(text(CrudQuery.READ_BY_NAME), 
                        {'user_name': user_name})
    return result.fetchall()

def get_users(db: Session):
    result = db.execute(text(CrudQuery.READ_ALL))
    return result.fetchall()

def create_user(db: Session, user: UserCreate):
    user_created_at = datetime.now()
    user_updated_at = user_created_at
    db.execute(
        text(CrudQuery.CREATE),
        {
            'user_name': user.user_name,
            'user_email': user.user_email,
            'user_password': user.user_password,
            'user_created_at': user_created_at,
            'user_updated_at': user_updated_at,
            'user_status': 'ACTIVE'
        }
    )
    db.commit()
    return get_user_by_email(db, user.user_email)

def update_user(db: Session, user_id: int, user: UserUpdate):
    # Fetch the current user from the database
    db_user = get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Define the update dictionary with values passed or default to existing values
    update_data = {
        'user_name': user.user_name if user.user_name else db_user.user_name,
        'user_email': user.user_email if user.user_email else db_user.user_email,
        'user_password': user.user_password if user.user_password else db_user.user_password,
        'user_updated_at': datetime.now(),
        'user_status': user.user_status if user.user_status else db_user.user_status
    }

    update_data['user_id'] = user_id
    db.execute(text(CrudQuery.UPDATE),update_data)
    db.commit()

    # Return the updated user
    return get_user_by_id(db, user_id)

def delete_user(db: Session, user_id: int):
    user_updated_at = datetime.now()
    db.execute(
        text(CrudQuery.DELETE),
        {'user_updated_at': user_updated_at, 'user_id': user_id}
    )
    db.commit()
    return get_user_by_id(db, user_id)

