from fastapi import HTTPException
from models.programming import Programming
from models.design import Design
from models.trading import Trading
from utils.db_operations import get_in_db
from models.likes import Likes
from sqlalchemy.orm import joinedload


def get_likes(db, user):
    if user:
        return db.query(Likes).options(joinedload(Likes.programming), joinedload(Likes.trading),
                                       joinedload(Likes.design)).filter(Likes.user_id == user.id).all()


def create_likes(source, source_id, db, user):
    if user:
        if (source == "laptops" and db.query(Programming).filter(Programming.id == source_id).first() is None) or \
                    (source == "telephone" and db.query(Trading).filter(Trading.id == source_id).first() is None) or \
                    (source == "planshet" and db.query(Design).filter(Design.id == source_id).first() is None):
                raise HTTPException(400, "File biriktiriladigan obyekt topilmadi")

        if source_id is None:
            raise HTTPException(400, "Bunday id li ma'liumot yo'q")
        existing_like = db.query(Likes).filter(
            Likes.user_id == user.id,
            Likes.source == source,
            Likes.source_id == source_id
        ).first()
        if existing_like is None:
            new_item_db = Likes(
                user_id=user.id,
                source=source,
                source_id=source_id
                    )
            db.add(new_item_db)
            db.commit()
            if source == "laptops" and Programming.id == source_id:
                db.query(Programming).update({
                Programming.faworite: Programming.faworite + 1})
            db.commit()
            if source == "telephone" and Trading.id == source_id:
                db.query(Design).update({
                Trading.faworite: Trading.faworite + 1
                })
            db.commit()

            if source == "planshet" and Design.id == source_id:
                db.query(Design).update({
                Design.faworite: Design.faworite + 1
                })
            db.commit()


def delete_likes(ident, db, user):
    if user:
        get_in_db(db, Likes, ident)
        db.query(Likes).filter(Likes.id == ident).delete()
        db.commit()


def delete_all(db, user):
    if user:
        deleted_likes = db.query(Likes).filter(Likes.user_id == user.id).all()
        db.query(Likes).filter(Likes.user_id == user.id).delete()
        db.commit()
        return deleted_likes

