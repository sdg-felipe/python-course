from fastapi import FastAPI
import models
from db import engine
from routers import auth, todos, admin, users

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "healthy"}

app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(users.router)
app.include_router(todos.router)


