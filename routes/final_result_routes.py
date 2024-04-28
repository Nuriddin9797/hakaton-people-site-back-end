from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Universal_funksyalar.update_db import post_put_db
from db import database
from models.answers_model import Answers
from models.results_model import Result
from routes.login import get_current_active_user
from schemas.users import CreateUser
from models.final_result_model import Final_Result

routes_final_result = APIRouter(
    prefix="/final_result",
    tags=["Final_result operations"]
)


@routes_final_result.get("/get_final_result")
def get_all(db: Session = Depends(database),
        current_user: CreateUser = Depends(get_current_active_user)):
    forms = db.query(Result).filter(Result.user_id == current_user.id).all()
    total = 0
    currect = 0
    for form in forms:
        total += 1
        answer = post_put_db(db, Answers, form.answer_id)
        if answer.t_javob:
            currect += 1

    procent = currect // total * 100
    incomes_dict = {
        "All Answers": total,
        "Trues": currect,
        "Percentage": f"{procent}%",
    }
    return incomes_dict


@routes_final_result.get('/final_finally_result')
def final_finally_results(db: Session = Depends(database),
        current_user: CreateUser = Depends(get_current_active_user)):
    return db.query(Final_Result).all()


