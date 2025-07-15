from sqlalchemy import create_engine, StaticPool, text
from sqlalchemy.orm import sessionmaker
from starlette import status

from db import Base
from main import app
from routers.auth import get_current_user
from routers.todos import get_db
from fastapi.testclient import TestClient
import pytest
from models import Todos

SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_current_user():
    return {'username': 'override_user', 'id': 1, 'role': 'admin'}

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_current_user

client = TestClient(app)

@pytest.fixture
def test_todo():
    todo = Todos(
        title="test",
        description="test",
        priority=5,
        complete=False,
        owner_id=1
    )
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as conn:
        conn.execute(text("DELETE FROM todos"))
        conn.commit()

# NOT WORKING
def test_read_all_authenticated():
    response = client.get("/todos")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []