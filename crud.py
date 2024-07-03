from sqlalchemy.orm import Session
from sqlalchemy import text
from datetime import datetime
from schemas import UserCreate, UserUpdate
from typing import List
from fastapi import HTTPException

def get_user_by_id(db: Session, user_id: int):
    result = db.execute(text("SELECT * FROM users WHERE user_id = :user_id AND user_status != 'DELETED'"), {'user_id': user_id})
    return result.fetchone()

def get_user_by_email(db: Session, user_email: str):
    result = db.execute(text("SELECT * FROM users WHERE user_email = :user_email AND user_status != 'DELETED'"), {'user_email': user_email})
    return result.fetchone()

def get_user_by_name(db: Session, user_name: str):
    result = db.execute(text("SELECT * FROM users WHERE user_name = :user_name AND user_status != 'DELETED'"), {'user_name': user_name})
    return result.fetchall()

def get_users(db: Session):
    result = db.execute(text("SELECT * FROM users WHERE user_status != 'DELETED' ORDER BY user_id"))
    return result.fetchall()

def create_user(db: Session, user: UserCreate):
    user_created_at = datetime.now()
    user_updated_at = user_created_at
    db.execute(
        text("INSERT INTO users (user_name, user_email, user_password, user_created_at, user_updated_at, user_status) VALUES (:user_name, :user_email, :user_password, :user_created_at, :user_updated_at, :user_status)"),
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
    db.execute(text("UPDATE users SET user_name = :user_name, user_email = :user_email,user_password = :user_password, user_updated_at = :user_updated_at, user_status = :user_status WHERE user_id = :user_id"),update_data)
    db.commit()

    # Return the updated user
    return get_user_by_id(db, user_id)

def delete_user(db: Session, user_id: int):
    user_updated_at = datetime.now()
    db.execute(
        text("UPDATE users SET user_status = 'DELETED', user_updated_at = :user_updated_at WHERE user_id = :user_id"),
        {'user_updated_at': user_updated_at, 'user_id': user_id}
    )
    db.commit()
    return get_user_by_id(db, user_id)

#def get_user_by_email(db: Session, user_email: str):
#    result = db.execute(text("SELECT * FROM users WHERE user_email = :user_email"), {'user_email': user_email})
#    return result.fetchone()
