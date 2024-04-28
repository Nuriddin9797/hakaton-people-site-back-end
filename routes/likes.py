from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from function.likes import get_likes, create_likes, delete_likes, delete_all
from models.likes import Likes
from routes.login import get_current_active_user
from schemas.users import CreateUser
from schemas.likes import CreateLikes
from db import database


likes_router = APIRouter(
    prefix="/likes",
    tags=["Likes operation"]
)


@likes_router.get('/get_total')
def get_all_likes_count(db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    total_likes = db.query(func.count(Likes.id)).filter(
        Likes.user_id == current_user.id
    ).scalar()
    return total_likes


@likes_router.get('/get')
def get_like(db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    return get_likes(db, current_user)


@likes_router.post('/create')
def create(form: CreateLikes = Depends(CreateLikes), db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    create_likes(form.source, form.source_id, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@likes_router.delete("/delete")
def delete(ident: int = 0, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    delete_likes(ident, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@likes_router.delete('/delete_all')
def delete_all_likes(db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    delete_all(db, current_user)
    return {"message": "Barcha likelar muvaffaqiyatli o'chirildi"}




