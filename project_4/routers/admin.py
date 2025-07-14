from fastapi import APIRouter
from typing import Annotated

from fastapi.params import Path
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from models import Todos
from db import SessionLocal
from .auth import get_current_user

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/todos")
async def get_all(user: user_dependency, db: db_dependency):
    if user is None or user.get('role') != 'admin':
        raise HTTPException(status_code=403, detail="Forbidden")
    return db.query(Todos).all()

@router.delete("/todos/{id}")
async def delete(user: user_dependency, db: db_dependency, id: int = Path(gt=0)):
    if user is None or user.get('role') != 'admin':
        raise HTTPException(status_code=403, detail="Forbidden")
    todo_model = db.query(Todos).filter(Todos.id == id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="not found")
    db.delete(todo_model)
    db.commit()
