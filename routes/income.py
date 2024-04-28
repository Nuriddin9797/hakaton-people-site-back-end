from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from models.application import Application
from models.income import Income
from models.programming import Programming
from models.design import Design
from models.trading import Trading
from models.users import Users
from routes.login import get_current_active_user
from schemas.users import CreateUser
from db import database
';lkj '
income_router = APIRouter(
    prefix="/income",
    tags=["Income operation"]
)


@income_router.get('/get')
def get_incomes(db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    if current_user.role == "admin":
        if current_user.role == "admin":
            total_price = 0
            programming_price = 0
            design_price = 0
            trading_price = 0
            users = db.query(Users).all()
            for user in users:
                if user:
                    carts = db.query(Programming, Design, Trading).all()
                    for cart in carts:
                        if cart.source == "programming":
                            prog = db.query(Programming).filter(Programming.id == cart.source_id).first()
                            if prog:
                                programming_price += prog.price
                        elif cart.source == "trading":
                                trading = db.query(Trading).filter(Trading.id == cart.source_id).first()
                                if trading:
                                    trading_price += trading.price
                        elif cart.source == "design":
                            design = db.query(Design).filter(Design.id == cart.source_id).first()
                            if design:
                                design_price += design.price
                    total_price = programming_price + trading_price + design_price
                    new_income = Income(total_price=total_price, programming_price=programming_price,
                                        design_price=design_price, trading_price=trading_price)
                    db.add(new_income)
            db.commit()
            incomes_dict = {
                "total_price": total_price,
                "programming_price": programming_price,
                "design_price": design_price,
                "trading_price": trading_price
            }
            return incomes_dict


@income_router.get('/get_income_user')
def get_incomes_user(db: Session = Depends(database),
                      current_user: CreateUser = Depends(get_current_active_user)):
    if current_user.role == "admin":
        total_price = 0
        result = []
        users = db.query(Users).all()
        for user in users:
            user_total_price = 0
            programming_price = db.query(func.sum(Programming.price)).join(Application).filter(
                Application.user_id == user.id).scalar() or 0
            design_price = db.query(func.sum(Design.price)).join(Application).filter(
                Application.user_id == user.id).scalar() or 0
            trading_price = db.query(func.sum(Trading.price)).join(Application).filter(
                Application.user_id == user.id).scalar() or 0

            user_total_price = programming_price + design_price + trading_price
            total_price += user_total_price
            result.append({
                "user_id": user.id,
                "total_price": user_total_price,
                "programming_price": programming_price,
                "design_price": design_price,
                "trading_price": trading_price
            })

        new_income = Income(total_price=total_price)
        db.add(new_income)
        db.commit()

        return result
# @income_router.get('/get_income_user')
# def get_incomes_user(db: Session = Depends(database),
#                 current_user: CreateUser = Depends(get_current_active_user)):
#     if current_user.role == "admin":
#         total_price = 0
#         users = db.query(Users).all()
#         result = ""
#         for user in users:
#             programming_price = 0
#             design_price = 0
#             trading_price = 0
#             if user:
#                 user_total_price = 0
#                 carts = db.query(Programming, Trading, Design).all()
#                 for cart in carts:
#                     if cart.source == "laptop":
#                         laptop = db.query(Programming).filter(Programming.id == cart.source_id).first()
#                         if laptop:
#                             programming_price += laptop.price
#                     elif cart.source == "telephone":
#                         telephone = db.query(Design).filter(Design.id == cart.source_id).first()
#                         if telephone:
#                             design_price += telephone.price
#                     elif cart.source == "planshet":
#                         planshet = db.query(Trading).filter(Trading.id == cart.source_id).first()
#                         if planshet:
#                             trading_price += planshet.price
#                 user_total_price = trading_price + design_price + programming_price
#                 result += (f" User: {user.id}, Total price: {user_total_price}, "
#                            f"Programming price: {programming_price}, design price: {design_price}, "
#                            f"Trading price: {trading_price};")
#                 total_price += user_total_price
#         new_income = Income(total_price=total_price)
#         db.add(new_income)
#         db.commit()
#         incomes_dict = {
#             "user": user.id,
#             "total_price": total_price,
#             "programming_price": programming_price,
#             "design_price": design_price,
#             "trading_price": trading_price
#         }
#         return incomes_dict

