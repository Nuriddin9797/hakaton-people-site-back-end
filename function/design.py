from sqlalchemy.orm import joinedload
from utils.db_operations import get_in_db, save_in_db
from utils.pagination import pagination
from models.design import Design
from fastapi import HTTPException


def get_programming(ident, skill, page, limit, db):
    if ident > 0:
        pro_filter = Design.id == ident
        db.query(Design).filter(Design.id == ident).update({
            Design.see_num: Design.see_num + 1
        })
        db.commit()
    else:
        pro_filter = Design.id > 0
    if skill:
        search_formatted = "%{}%".format(skill)
        skill_filter = (Design.skill.like(search_formatted))
    else:
        skill_filter = Design.id > 0
    items = (db.query(Design).options(joinedload(Design.files)).filter(pro_filter,
                                                                         skill_filter).order_by(Design.id.desc()))

    return pagination(items, page, limit)


def create_programming(forms, db, user):
    for form in forms:
        if user.role == "admin":
            new_item_db = Design(
                experience=form.experience,
                skills=form.skills,
                see_num=0,
                jobs_id=form.id
            )
            save_in_db(db, new_item_db)


def update_programming(forms, db, user):
    for form in forms:
        if user.role == "admin":
            update = db.query(Design).filter(Design.id == form.ident).first()
            if not update:
                raise HTTPException(status_code=404, detail="Laptops topilmadi")
            db.query(Design).filter(Design.id == form.ident).update({
                Design.experience: form.experience,
                Design.skills: form.skills
            })
            db.commit()


def delete_programming(ident, db, user):
    if user.role == "admin":
        get_in_db(db, Design, ident)
        db.query(Design).filter(Design.id == ident).delete()
        db.commit()