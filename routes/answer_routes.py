from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import database
from function.answers_function import create_answer, delete_answer, update_answer
from schemas.answers_schemas import create_myanswer, update_myanswer
from models.answers_model import Answers
from schemas.users import CreateUser
from routes.login import get_current_active_user


router_answer = APIRouter(
    prefix="/answer",
    tags=["Answer operations"]
)


@router_answer.post('/create')
def create(forms: List[create_myanswer],
           db: Session = Depends(database),
        current_user: CreateUser = Depends(get_current_active_user)):
    create_answer(forms, db, current_user)
    raise HTTPException(200, "amaliyot muvaffaqiyatli yakunlandi!")


@router_answer.get('/get')
def get(db: Session = Depends(database),
        current_user: CreateUser = Depends(get_current_active_user)):
    answer = db.query(Answers).all()
    return answer


@router_answer.put('/update')
def update(forms: List[update_myanswer], db: Session = Depends(database),
        current_user: CreateUser = Depends(get_current_active_user)):
    update_answer(forms, db, current_user)
    raise HTTPException(200, "yangilash muvaffaqiyatli malga oshirildi!")


@router_answer.delete('/delete')
def delete(ident: int = 0, db: Session = Depends(database),
        current_user: CreateUser = Depends(get_current_active_user)):
    delete_answer(ident, db, current_user)
    raise HTTPException(200, "O'chirish muvaffaqiyatli amalga oshirildi!")