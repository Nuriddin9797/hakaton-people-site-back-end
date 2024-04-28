from fastapi import HTTPException
from utils.db_operations import save_in_db
from utils.pagination import pagination
from models.jobs import Jobs


def get_jobs(ident, search, page, limit, db):
    if ident > 0:
        ident_filter = Jobs.id == ident
    else:
        ident_filter = Jobs.id > 0
    if search:
        search_formatted = "%{}%".format(search)
        search_filter = (Jobs.name.like(search_formatted))
    else:
        search_filter = Jobs.id > 0
    items = db.query(Jobs).filter(ident_filter, search_filter).order_by(Jobs.id.desc())
    return pagination(items, page, limit)


def create_jobs(form, db, user):
    if user.role == "admin":
        new_item_db = Jobs(
            name=form.name
        )
        save_in_db(db, new_item_db)


def update_jobs(form, db, user):
    if user.role == "admin":
        category = db.query(Jobs).filter(Jobs.id == form.ident).first()
        if not category:
            raise HTTPException(status_code=404, detail="Kategoriya topilmadi")

        db.query(Jobs).filter(Jobs.id == form.ident).update({
            Jobs.name: form.name
    })
    db.commit()


def delete_jobs(ident, db, user):
    if user.role == "admin":
        jobs = db.query(Jobs).filter(Jobs.id == ident).first()
        if not jobs:
            raise HTTPException(status_code=404, detail="Kategoriya topilmadi")
    db.query(Jobs).filter(Jobs.id == ident).delete()
    db.commit()