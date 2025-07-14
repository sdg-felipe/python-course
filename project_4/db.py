from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

'''
SQLITE3 DB

SQLALCHEMY_DATABASE_URI = "sqlite:///./todosapp.db"
engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False})


POSTGRES DB

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost/TodoAppDB"
engine = create_engine(SQLALCHEMY_DATABASE_URI)


MYSQL DB

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:admin@localhost:3306/todoappdb"
engine = create_engine(SQLALCHEMY_DATABASE_URI)
'''

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@localhost:3306/todoappdb"
engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()