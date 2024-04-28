import inspect
from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session, aliased
from function.cart import get_cart, create_cart, delete_cart, update_carts
from models.cart import Carts
from routes.login import get_current_active_user
from schemas.cart import CreateCarts, UpdateCarts
from schemas.users import CreateUser
from db import database


cart_router = APIRouter(
    prefix="/cart",
    tags=["Cart operation"]
)


@cart_router.get('/get_total')
def get_all_cart_count(db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    total_carts = db.query(func.count(Carts.id)).scalar()
    return total_carts


@cart_router.get('/get')
def get(db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    return get_cart(db, current_user)


@cart_router.post('/create')
def create(forms: List[CreateCarts] = Depends(CreateCarts), db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    create_cart(forms, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@cart_router.put('/confirmation')
def update(ident: int = 0, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    update_carts(ident, current_user, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@cart_router.delete("/delete")
def delete(ident: int = 0, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    delete_cart(ident, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


