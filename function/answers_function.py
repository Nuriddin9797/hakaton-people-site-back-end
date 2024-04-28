from Universal_funksyalar.update_db import post_put_db
from models.answers_model import Answers
from fastapi import HTTPException
from models.questions_model import Question
from models.users import Users


def create_answer(forms, db, user):
    if user.role == "admin":
        for form in forms:
            post_put_db(db, Question, form.question_id)
            new_item_db = Answers(
                answer=form.answer,
                t_javob=form.t_javob,
                question_id=form.question_id
            )
            db.add(new_item_db)
            db.commit()
            db.refresh(new_item_db)


def update_answer(forms, db, user):
    if Users.role == "admin":
        for form in forms:
            updatequestion = db.query(Answers).filter(Answers.id == form.ident).first()
            if updatequestion is None:
                raise HTTPException(400, "id bo'yicha ma'lumot topilmadi")
            db.query(Answers).filter(Answers.id == user.id).update({
                Answers.answer: form.answer,
                Answers.question_id: form.question_id
            })
        db.commit()


def delete_answer(ident, db, user):
    if user.role == "admin":
        delete = db.query(Answers).filter(Answers.id == ident).first()
        if delete is None:
            raise HTTPException(400, "Bunday id li javob yo'q")
        db.query(Answers).filter(Answers.id == user.id).delete()
    db.commit()
    return {"message": "Ma'lumotlaringiz o'chirildi"}