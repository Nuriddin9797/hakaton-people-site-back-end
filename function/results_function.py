from models.categories_model import Categories
from models.results_model import Result
from models.answers_model import Answers
from Universal_funksyalar.update_db import post_put_db
from models.users import Users
from models.final_result_model import Final_Result


def create_result(forms, db, user):
    hamma_savollar = 0
    t_javoblar = 0
    for form in forms:
        new_item_db = Result(
            question_id=form.question_id,
            category_id=form.category_id,
            answer_id=form.answer_id,
            user_id=user.id
        )
        db.add(new_item_db)
        db.commit()
        db.refresh(new_item_db)

        hamma_savollar += 1
        answer = post_put_db(db, Answers, form.answer_id)
        if answer.t_javob:
            t_javoblar += 1

    foiz = t_javoblar / hamma_savollar * 100

    final_results = Final_Result(
        hamma_savollar=hamma_savollar,
        t_javoblar=t_javoblar,
        foiz=foiz,
        user_id=user.id
    )

    db.add(final_results)
    db.commit()
    db.refresh(final_results)

    return f"umumiy: {hamma_savollar}, topildi: {t_javoblar}, foizda: {foiz}"


def get_result(db, user):
    final_result = db.query(Result).filter(Result.user_id == user.id).order_by(Result.id.desc()).first()
    if final_result:
        category_name = final_result.category.name
        if category_name == "trading":
            return "Siz uchun trading"
    return "Natija topilmadi yoki mavjud emas"

