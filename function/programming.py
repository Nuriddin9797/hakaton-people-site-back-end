from sqlalchemy.orm import joinedload
from utils.db_operations import get_in_db, save_in_db
from utils.pagination import pagination
from models.programming import Programming
from fastapi import HTTPException


def get_programming(ident, skills, page, limit, db):
    if ident > 0:
        pro_filter = Programming.id == ident
        db.query(Programming).filter(Programming.id == ident).update({
            Programming.see_num: Programming.see_num + 1
        })
        db.commit()
    else:
        pro_filter = Programming.id > 0
    if skills:
        search_formatted = "%{}%".format(skills)
        skill_filter = (Programming.skills.like(search_formatted))
    else:
        skill_filter = Programming.id > 0
    items = (db.query(Programming).options(joinedload(Programming.files)).filter(pro_filter,
                                                                         skill_filter).order_by(Programming.id.desc()))

    return pagination(items, page, limit)


def create_programming(forms, db, user):
    if user:
        for form in forms:
            new_item_db = Programming(
                name=form.name,
                experience=form.experience,
                skills=form.skills,
                level=form.level,
                see_num=0,
                jobs_id=form.jobs_id
                )
            save_in_db(db, new_item_db)


def update_programming(forms, db, user):
    for form in forms:
        update = db.query(Programming).filter(Programming.id == form.ident).first()
        if not update:
            raise HTTPException(status_code=404, detail="Laptops topilmadi")
        db.query(Programming).filter(Programming.id == form.ident).update({
            Programming.name: form.name,
            Programming.experience: form.experience,
            Programming.skills: form.skills
            })
        db.commit()


def delete_programming(ident, db, user):
    if user.role == "admin":
        get_in_db(db, Programming, ident)
        db.query(Programming).filter(Programming.id == ident).delete()
        db.commit()