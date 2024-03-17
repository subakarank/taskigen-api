# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .database_config import SQLALCHEMY_DATABASE_URL

# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Define a function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()