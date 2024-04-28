from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from db import database
from function.programming import get_programming, update_programming, create_programming, delete_programming
from models.programming import Programming
from routes.login import get_current_active_user
from schemas.programming import CreateProgramming, UpdateProgramming
from schemas.users import CreateUser

programming_router = APIRouter(
    prefix="/programming_router",
    tags=["Programming_router operation"]
)


@programming_router.get('/get_filter')
def get(ident: int = 0, skills: str = None, page: int = 1, limit: int = 25, db: Session = Depends(database)):
    a = get_programming(ident, skills, page, limit, db)
    return a


@programming_router.post('/create')
def create(forms: List[CreateProgramming], db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    create_programming(forms, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@programming_router.put("/update")
def update(forms: List[UpdateProgramming], db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    update_programming(forms, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@programming_router.delete("/delete")
def delete(db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    delete_programming(db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


