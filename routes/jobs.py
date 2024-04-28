import random
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from function.jobs import get_jobs, create_jobs, update_jobs, delete_jobs
from models.design import Design
from models.programming import Programming
from models.trading import Trading
from routes.login import get_current_active_user
from schemas.jobs import CreateJobs, UpdateJobs
from schemas.users import CreateUser
from db import database

jobs_router = APIRouter(
    prefix="/Jobs",
    tags=["Jobs operation"]
)


@jobs_router.get('/get_all')
def get_all_jobs(db: Session = Depends(database)):
    trading = db.query(Trading).all()
    programming = db.query(Programming).all()
    design = db.query(Design).all()
    items = trading + programming + design
    random.shuffle(items)
    return items


@jobs_router.get('/get')
def get(ident: int = 0, search: str = None,  page: int = 1,
                 limit: int = 25, db: Session = Depends(database)):
    return get_jobs(ident, search, page, limit, db)


@jobs_router.post('/create')
def create(form: CreateJobs, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    create_jobs(form, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@jobs_router.put("/update")
def update(form: UpdateJobs, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    update_jobs(form, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@jobs_router.delete("/delete")
def delete(ident: int = 0, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    delete_jobs(ident, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")