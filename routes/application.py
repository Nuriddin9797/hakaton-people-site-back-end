from typing import List
from function.application import create_application, delete_application
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from models.application import Application
from routes.login import get_current_active_user
from schemas.application import Create_Application
from schemas.users import CreateUser
from db import database

application_router = APIRouter(
    prefix="/application",
    tags=["Application operation"]
)


@application_router.get('/get_total')
def get_all_count(db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    total_likes = db.query(func.count(Application.id)).filter(
        Application.user_id == current_user.id
    ).scalar()
    return total_likes


@application_router.get('/get')
def get_application(user: CreateUser = Depends(get_current_active_user), db: Session = Depends(database)):
    orders = db.query(Application).filter(Application.user_id == user.id).all()
    return orders


@application_router.post('/create')
def create(form: CreateUser = Depends(Create_Application), db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    create_application(form.carts_id, form.name, form.user_name, form.city, form.district, form.address, form.tel_number,db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@application_router.delete("/delete")
def delete(ident: int = 0, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    delete_application(ident, db, current_user)
    return {"message": "Buyurtma muvaffaqiyatli o'chirildi"}
