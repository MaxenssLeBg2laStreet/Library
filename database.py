from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_NAME = "./database/library.db"
SQLALCHEMY_DATABASE_URL = "sqlite:///{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args = {"check_same_thread": False}
)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() :
    db = SessionLocal()
    try :
        yield db
    finally:
        db.close()

def init_db() :
    Base.metadata.creat_all(bind=engine)
