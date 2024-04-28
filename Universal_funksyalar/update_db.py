from fastapi import HTTPException
def post_put_db(db, model, ident):
    text = db.query(model).filter(model.id == ident).first()
    if text is None:
        raise HTTPException(400, f"{model}dan ma'lumot topilmadi!")
    return text
