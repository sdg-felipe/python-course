from datetime import timedelta, datetime, timezone
from http.client import HTTPException

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from db import SessionLocal
from models import Users
from passlib.context import CryptContext
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

JWT_SECRET_KEY = '14cba3c7fc2430589f638666d39792af878f52ec82a2755f27bd936db8b0e16c'

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

def auth_user(username: str, password: str, db: db_dependency):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.password):
        return False
    return user

def create_access_token(username: str, user_id: int, role: str, expires_delta: timedelta):
    expire = datetime.now(timezone.utc) + expires_delta

    to_encode = {
        "username": username,
        "id": user_id,
        "role": role,
        "expires": expire.isoformat(),
    }
    return jwt.encode(to_encode, JWT_SECRET_KEY)


async def get_current_user(token: str = Depends(oauth2_bearer)):

    try:
        payload = jwt.decode(token, JWT_SECRET_KEY)
        username: str = payload.get("username")
        user_id: int = payload.get("id")
        role: str = payload.get("role")
        if username is None or user_id is None:
            raise HTTPException(status_code=404, detail='could not verify token')
        return {'username': username, 'id': user_id, 'role': role}
    except JWTError:
        raise HTTPException(status_code=401, detail='could not verify token')


class CreateUserRequest(BaseModel):
    username: str
    password: str
    email: str
    role: str
    phone_number: str


@router.post("/")
async def create_user(db: db_dependency, new_user: CreateUserRequest):
    user_model = Users(
        email=new_user.email,
        username=new_user.username,
        password= bcrypt_context.hash(new_user.password),
        role=new_user.role,
        is_active=True,
        phone_number=new_user.phone_number,
    )

    db.add(user_model)
    db.commit()

@router.post("/token")
async def create_token(db:db_dependency,form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = auth_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=401, detail='could not validate user')
    token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))
    return {'access_token': token, 'token_type': 'bearer'}
