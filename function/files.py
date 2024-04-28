import os
from fastapi import HTTPException
from models.files import Files
from models.users import Users
from models.programming import Programming
from models.design import Design
from models.trading import Trading
from utils.db_operations import get_in_db


def create_file(new_files, source, source_id, db, current_user):
    if current_user:
        if (source == "programming" and db.query(Programming).filter(Programming.id == source_id).first() is None) or \
                (source == "users" and db.query(Users).filter(Users.id == source_id).first() is None) or \
                (source == "trading" and db.query(Trading).filter(Trading.id == source_id).first() is None) or \
                (source == "support" and db.query(Trading).filter(Trading.id == source_id).first() is None) or \
                (source == "application" and db.query(Trading).filter(Trading.id == source_id).first() is None) or \
                (source == "design" and db.query(Design).filter(Design.id == source_id).first() is None):
            raise HTTPException(400, "File biriktiriladigan obyekt topilmadi")
        uploaded_file_objects = []
        for new_file in new_files:
            ext = os.path.splitext(new_file.filename)[-1].lower()
            if ext not in [".jpg", ".png", ".mp3", ".mp4", ".gif", ".jpeg"]:
                raise HTTPException(400,"Yuklanadigan fayl formati mos emas")
            file_location = f"files/{new_file.filename}"
            with open(file_location, "wb+") as file_objects:
                file_objects.write(new_file.file.read())

            new_item_db = Files(
                file=new_file.filename,
                source=source,
                source_id=source_id
            )
            uploaded_file_objects.append(new_item_db)
        db.add_all(uploaded_file_objects)
        db.commit()


def delete_files(ident, db, user):
    if user.role == "admin":
        get_in_db(db, Files, ident)
        db.query(Files).filter(Files.id == ident).delete()
        db.commit()


def update_files(new_files, source, source_id, user, db):
    if user.role == "admin":
        items = db.query(Files).filter(Files.source == source,
                                       Files.source_id == source_id).all()
        for item in items:
            delete_files(item.id, db, user)
            create_file(new_files, source, source_id, user, db)