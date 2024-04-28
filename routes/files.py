from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from function.files import create_file, update_files, delete_files
from routes.login import get_current_active_user
from schemas.files import CreateFile
from schemas.users import CreateUser
from db import database


files_router = APIRouter(
    prefix="/files",
    tags=["Files operation"]
)


@files_router.post('/create')
def create(form: CreateFile = Depends(CreateFile),
           db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    create_file(form.new_files, form.source, form.source_id, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@files_router.put("/update")
def update(form: CreateFile = Depends(CreateFile),
           db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    update_files(form.new_files, form.source, form.source_id, current_user, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@files_router.delete("/delete")
def delete(ident: int, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    delete_files(ident, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


