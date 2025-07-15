from fastapi import APIRouter
from typing import Annotated

from fastapi.params import Path
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from models import Todos
from db import SessionLocal
from .auth import get_current_user

router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


class TodoRequest(BaseModel):
    title: str  = Field(min_length=3)
    description: str = Field(min_length=3, max_length=1000)
    priority: int = Field(gt=0, lt=10)
    complete: bool


@router.get("/")
async def get_all(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='auth failed')

    return db.query(Todos).filter(Todos.owner_id == user.get('id')).all()

@router.get("/{id}")
async def get_todo(user: user_dependency, db: db_dependency,id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='auth failed')

    todo_model = (db.query(Todos).filter(Todos.id == id)\
                  .filter(Todos.owner_id == user.get('id')).first())
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail='Todo not found')

@router.post("/")
async def create_todo(user: user_dependency, db:db_dependency, todo: TodoRequest):
    if user is None:
        raise HTTPException(status_code=401, detail='auth failed')

    todo_model = Todos(**todo.model_dump(), owner_id=user.get('id'))

    db.add(todo_model)
    db.commit()

@router.put("/{id}")
async def update_todo(user: user_dependency, db: db_dependency, todo: TodoRequest, id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='auth failed')

    todo_model = (db.query(Todos).filter(Todos.id == id)\
                  .filter(Todos.owner_id == user.get('id')).first())
    if todo_model is None:
        raise HTTPException(status_code=404, detail='todo not found')

    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete

    db.add(todo_model)
    db.commit()

@router.delete("/{id}")
async def delete_todo(user: user_dependency, db: db_dependency, id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='auth failed')

    todo_model = (db.query(Todos).filter(Todos.id == id)\
                  .filter(Todos.owner_id == user.get('id')).first())
    if todo_model is None:
        raise HTTPException(status_code=404, detail='todo not found')

    db.delete(todo_model)
    db.commit()