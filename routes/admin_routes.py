from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from function.users import create_user_f
from routes.login import get_current_user
from schemas.users import CreateUser, Users
from db import database

admin_router = APIRouter(
    prefix="/admin",
    tags=["Admin Operations"]
)


def get_current_admin_user(current_user: Users = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=400, detail="Sizda huquq yo'q")
    return current_user


@admin_router.get('/get_admin')
def get_users_as_admin(db: Session = Depends(database),
                       current_admin_user: Users = Depends(get_current_admin_user)):
        users = db.query(Users).filter(Users.role == "admin").all()
        return users


@admin_router.post('/create_admin')
def create_user_as_admin(form: CreateUser, db: Session = Depends(database),
                       current_admin_user: Users = Depends(get_current_admin_user)):
    if current_admin_user.role == "admin":
        create_user_f(form, db, current_admin_user)
        raise HTTPException(status_code=200, detail="Foydalanuvchi muvaffaqiyatli yaratildi")
    else:
        raise HTTPException(400, "Sizga ruhsat berilmagan")

