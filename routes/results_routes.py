from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import database
from function.results_function import create_result
from models.results_model import Result
from routes.login import get_current_active_user
from schemas.results_schema import create_myresult
from schemas.users import CreateUser

router_result = APIRouter(
    prefix="/result",
    tags=["Result operations"]
)


@router_result.post('/create')
def create(forms: List[create_myresult], db: Session = Depends(database),
        current_user: CreateUser = Depends(get_current_active_user)):
    create_result(forms, db, current_user)
    raise HTTPException(200, "amaliyot muvaffaqiyatli yakunlandi!")


@router_result.get('/get')
def get(db: Session = Depends(database),
        current_user: CreateUser = Depends(get_current_active_user)):
    users = db.query(Result).filter(Result.user_id == current_user.id).all()
    return users
