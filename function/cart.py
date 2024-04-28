from fastapi import HTTPException
from models.programming import Programming
from models.trading import Trading
from models.design import Design
from utils.db_operations import get_in_db
from models.cart import Carts


def get_cart(db, user):
    if user:
        all = db.query(Carts).filter(Carts.user_id == user.id).all()
        return all


def create_cart(form, db, user):
    if user:
        if (form.source == "laptops" and db.query(Programming).filter(Programming.id == form.source_id).first() is None) or \
                (form.source == "telephone" and db.query(Design).filter(Design.id == form.source_id).first() is None) or \
                (form.source == "planshet" and db.query(Trading).filter(Trading.id == form.source_id).first() is None):
            raise HTTPException(400, "File biriktiriladigan obyekt topilmadi")

        new_item_db = Carts(
            user_id=user.id,
            source=form.source,
            source_id=form.source_id,
            amount=form.amount,
            status=False
                )
        db.add(new_item_db)
        db.commit()


def update_carts(ident, current_user, db):
    if current_user and current_user.role == "admin":
        order_to_update = db.query(Carts).filter(Carts.id == ident).first()
        if order_to_update is None:
            raise HTTPException(status_code=404, detail="Order not found")

        db.query(Carts).filter(Carts.id == ident).update({Carts.status: True})
        db.commit()

        order = db.query(Carts).filter(Carts.id == ident, Carts.status == True).first()
        if order:
            carts = db.query()
            if carts:
                if carts.source == "laptop":
                    laptop = db.query(Programming).filter(Programming.id == carts.source_id, Programming.amount > 0).first()
                    if laptop:
                        db.query(Programming).filter(Programming.id == laptop.id).update({Programming.amount: Programming.amount - 1})
                elif carts.source == "telephone":
                    telephone = db.query(Design).filter(Design.id == carts.source_id,
                                                            Design.amount > 0).first()
                    if telephone:
                        db.query(Design).filter(Design.id == telephone.id).update(
                            {Design.amount: Design.amount - 1})
                elif carts.source == "planshet":
                    trading = db.query(Trading).filter(Trading.id == carts.source_id, Trading.amount > 0).first()
                    if trading:
                        db.query(Trading).filter(Trading.id == Trading.id).update(
                            {Trading.amount: Trading.amount - 1})
            db.commit()
        return "Order status updated successfully"
    else:
        return "User is not authorized to perform this action"


def delete_cart(ident, db, current_user):
    if current_user:
        get_in_db(db, Carts, ident)
        delete = db.query(Carts).filter(Carts.id == ident).delete()
        if delete:
            Carts.amount=-1
        db.commit()

