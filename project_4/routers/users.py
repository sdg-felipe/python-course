from fastapi import APIRouter
from typing import Annotated

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from models import Users
from db import SessionLocal
from .auth import get_current_user
from passlib.context import CryptContext

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get("/")
async def get_user(user:user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db.query(Users).filter(Users.id == user.get('id')).first()

@router.put("/password")
async def change_password(user:user_dependency, db: db_dependency, old_password: str, new_password: str):
    if user is None:
        raise HTTPException(status_code=401, detail="Auth failed")
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()

    if not bcrypt_context.verify(old_password, user_model.password):
        raise HTTPException(status_code=401, detail="Error on password change")

    user_model.password = bcrypt_context.encrypt(new_password)
    db.add(user_model)
    db.commit()