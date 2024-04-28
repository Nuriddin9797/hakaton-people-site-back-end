from routes.login import get_password_hash
from utils.db_operations import save_in_db
from models.users import Users


def create_user_f(form, db):
    new_item_db = Users(
        name=form.name,
        username=form.username,
        password=get_password_hash(form.password),
        skills=form.skills,
        level=form.level,
        role="user",
        token="Nuriddin",
        )
    save_in_db(db, new_item_db)


def create_general_user_f(form, db):
    # if user.role == "admin":
        new_item_db = Users(
            name=form.name,
            username=form.username,
            password=get_password_hash(form.password),
            skills=form.skills,
            level=form.level,
            token="Nuriddin",
            role="admin")

        save_in_db(db, new_item_db)


def update_user_f(form, db, user):
    db.query(Users).filter(Users.id == user.id).update({
        Users.name: form.name,
        Users.username: form.username,
        Users.password: get_password_hash(form.password),
        Users.role: user.role,
        Users.phone_number: form.phone_number
    })
    db.commit()


def delete_user_f(db, user):
    db.query(Users).filter(Users.id == user.id).delete()
    db.commit()


