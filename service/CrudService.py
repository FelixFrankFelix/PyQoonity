from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List,Union
from model.request import CrudRequest
from model.response import CrudResponse
from repository.database import CrudRepository
from db import SessionLocal, engine
from utility.exceptions import ResponseConstant


def create_user_service(body):
    if not body:
        return {
        "responseCode": ResponseConstant.DUPLICATE_RECORD.responseCode,
        "responseMessage": "email already exist", 
        }
    return {
        "responseCode": ResponseConstant.SUCCESS.responseCode,
        "responseMessage": ResponseConstant.SUCCESS.responseMessage, 
        "body" : body
        }


def read_users_service(body):
    return {
        "responseCode": ResponseConstant.SUCCESS.responseCode,
        "responseMessage": ResponseConstant.SUCCESS.responseMessage, 
        "body" : body
        }


def read_user_by_id_service(body):
    if body is None:
        return ResponseConstant.NO_SUCH_ISSUER
    return {
        "responseCode": ResponseConstant.SUCCESS.responseCode,
        "responseMessage": ResponseConstant.SUCCESS.responseMessage, 
        "body" : body
        }


def read_user_by_email_service(body):
    if body is None:
        return ResponseConstant.NO_SUCH_ISSUER
    return {
        "responseCode": ResponseConstant.SUCCESS.responseCode,
        "responseMessage": ResponseConstant.SUCCESS.responseMessage, 
        "body" : body
        }


def read_user_by_name_service(body):
    if not body:
        return ResponseConstant.NO_SUCH_ISSUER
    return {
        "responseCode": ResponseConstant.SUCCESS.responseCode,
        "responseMessage": ResponseConstant.SUCCESS.responseMessage, 
        "body" : body
        }
        



def update_user_service(body):
    if body is None:
        return ResponseConstant.NO_SUCH_ISSUER
    return {
        "responseCode": ResponseConstant.SUCCESS.responseCode,
        "responseMessage": ResponseConstant.SUCCESS.responseMessage, 
        "body" : body
        }


def delete_user_service(body):
    if body is None:
        return ResponseConstant.NO_SUCH_ISSUER
    return {
        "responseCode": ResponseConstant.SUCCESS.responseCode,
        "responseMessage": ResponseConstant.SUCCESS.responseMessage, 
        "body" : body
        }


