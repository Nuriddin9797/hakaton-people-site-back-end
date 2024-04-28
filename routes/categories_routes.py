from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from models.categories_model import Categories
from db import database
from function.categories_function import create_categories, delete_categories, update_categories, get_all_categories
from models.users import Users
from schemas.categories_schema import create_mycategories, update_mycategories
from routes.login import get_current_active_user
from schemas.users import CreateUser

router_categories = APIRouter(
    prefix="/Categories",
    tags=["Test Categories operations"]
)


@router_categories.post('/create')
def create(forms: List[create_mycategories], db: Session = Depends(database),
        current_user: CreateUser = Depends(get_current_active_user)):
    create_categories(forms, db, current_user)
    return {"message": "amaliyot muvaffaqiyatli yakunlandi!"}


@router_categories.get('/get')
def get_categories(db: Session = Depends(database)):
    categories = db.query(Categories).all()
    return categories


@router_categories.put('/update')
def update(forms: List[update_mycategories], db: Session = Depends(database),
                current_user: Users = Depends(get_current_active_user)):
    update_categories(forms, db, current_user)
    raise HTTPException(200, "yangilash muvaffaqiyatli amalga oshirildi!")


@router_categories.delete('/delete')
def delete(ident, db: Session = Depends(database),
                current_user: Users = Depends(get_current_active_user)):
    delete_categories(ident, db, current_user)
    raise HTTPException(200, "O'chirish muvaffaqiyatli amalga oshirildi!")