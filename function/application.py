from utils.db_operations import save_in_db
from models.application import Application
from fastapi import HTTPException


def create_application(forms, db, user):
    if user:
        for form in forms:
            new_item_db = Application(
                user_id=user.id,
                phone_number=form.phone_number,
                gmail=form.gmail,
                file=form.file,
                carts_id=form.carts_id
            )
            save_in_db(db, new_item_db)


def update_application(ident, db, user):
    if user.role == "admin":
        update = db.query(Application).filter(Application.id == ident).first()
        if not update:
            raise HTTPException(status_code=404, detail="Ariza topilmadi")
        db.query(Application).filter(Application.id == ident).update({
            Application.status: update.status,
        })
        db.commit()


def delete_application(ident, db, user):
    if user:
        order_to_delete = db.query(Application).filter(Application.id == ident and Application.user_id == user.id).first()
        if order_to_delete is None:
            raise HTTPException(400, "Application not found")
        db.delete(order_to_delete)
        db.commit()
        return {"message": "Application successfully deleted"}