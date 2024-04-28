from sqlalchemy.orm import joinedload
from utils.db_operations import get_in_db, save_in_db
from utils.pagination import pagination
from models.trading import Trading
from fastapi import HTTPException


def get_programming(ident, skill, page, limit, db):
    if ident > 0:
        pro_filter = Trading.id == ident
        db.query(Trading).filter(Trading.id == ident).update({
            Trading.see_num: Trading.see_num + 1
        })
        db.commit()
    else:
        pro_filter = Trading.id > 0
    if skill:
        search_formatted = "%{}%".format(skill)
        skill_filter = (Trading.skill.like(search_formatted))
    else:
        skill_filter = Trading.id > 0
    items = (db.query(Trading).options(joinedload(Trading.files)).filter(pro_filter,
                                                                         skill_filter).order_by(Trading.id.desc()))

    return pagination(items, page, limit)


def create_programming(forms, db, user):
    for form in forms:
        if user.role == "admin":
            new_item_db = Trading(
                experience=form.experience,
                skills=form.skills,
                see_num=0,
                jobs_id=form.id
            )
            save_in_db(db, new_item_db)


def update_programming(forms, db, user):
    for form in forms:
        if user.role == "admin":
            update = db.query(Trading).filter(Trading.id == form.ident).first()
            if not update:
                raise HTTPException(status_code=404, detail="Laptops topilmadi")
            db.query(Trading).filter(Trading.id == form.ident).update({
                Trading.experience: form.experience,
                Trading.skills: form.skills
            })
            db.commit()


def delete_programming(ident, db, user):
    if user.role == "admin":
        get_in_db(db, Trading, ident)
        db.query(Trading).filter(Trading.id == ident).delete()
        db.commit()