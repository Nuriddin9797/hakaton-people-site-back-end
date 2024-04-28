from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.questions_model import Question
from db import database
from function.questions_function import create_question, delete_question, update_question
from schemas.users import CreateUser
from routes.login import get_current_active_user
from schemas.questions_schema import create_myquestion, update_myquestion


router_question = APIRouter(
    prefix="/question",
    tags=["Question operations"]
)


@router_question.post('/create')
def create(forms: List[create_myquestion], db: Session = Depends(database),
        current_user: CreateUser = Depends(get_current_active_user)):
    create_question(forms, db, current_user)
    raise HTTPException(200, "amaliyot muvaffaqiyatli yakunlandi!")


@router_question.get('/get')
def get_questions(db: Session = Depends(database),
        current_user: CreateUser = Depends(get_current_active_user)):
    question = db.query(Question).all()
    return question


@router_question.put('/update')
def update(forms: List[update_myquestion], db: Session = Depends(database),
        current_user: CreateUser = Depends(get_current_active_user)):
    update_question(forms, db, current_user)
    raise HTTPException(200, "yangilash muvaffaqiyatli malga oshirildi!")


@router_question.delete('/delete')
def delete(ident, db: Session = Depends(database),
        current_user: CreateUser = Depends(get_current_active_user)):
    delete_question(ident, db, current_user)
    raise HTTPException(200, "O'chirish muvaffaqiyatli amalga oshirildi!")