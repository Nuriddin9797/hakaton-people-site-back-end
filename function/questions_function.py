from Universal_funksyalar import user_id
from models.questions_model import Question
from fastapi import HTTPException
from models.users import Users


def create_question(forms, db, user):
    if user.role in ["admin", "user"]:
        for form in forms:
            db.query(Question).filter(Question.question == user.id).first()
            new_item_db = Question(
                question=form.question,
                categoriya_id=form.categoriya_id
        )
            db.add(new_item_db)
            db.commit()
            db.refresh(new_item_db)


def get(db, current_user):
    if current_user.role == "admin" or current_user.id == user_id:
        user = db.query(Users).filter(Users.id == user_id).first()
        if user:
            return user


def update_question(forms, db, user):
    if user.role in ["admin", "user"]:
        for form in forms:
            question = db.query(Question).filter(Question.id == user.id).first()
            if question is None:
                raise HTTPException(400, "ID bo'yicha ma'lumot topilmadi")
            db.query(Question).filter(Question.id == user.id).update({
                Question.question: form.question,
                Question.categoriya_id: form.categoriya_id
            })
        db.commit()


def delete_question(ident, db, user):
    if user.role in ["admin", "user"]:
        question = db.query(Question).filter(Question.id == ident).first()
        if not question:
            raise HTTPException(status_code=400, detail="Berilgan IDga ega bo'lgan savol topilmadi")
        db.query(Question).filter(Question.id == user.id).delete()
        db.commit()
