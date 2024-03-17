# crud/user_crud.py

from sqlalchemy.orm import Session
from models.user_model import UserModel
from schemas.user_schema import UserSchema
from datetime import datetime, UTC


def create_user(db: Session, user_data: UserSchema) -> UserModel:
  # Create a new user instance using data from the UserSchema
  db_user = UserModel(
      email=user_data.email,
      name=user_data.name,
      password=user_data.password,
      status=user_data.status,
)
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  print(db_user)
  return db_user

def get_user(db: Session, user_id: int):
  return db.query(UserModel).filter(UserModel.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
  return db.query(UserModel).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, user_data: UserSchema):
  db_user = db.query(UserModel).filter(UserModel.id == user_id).first()

  if db_user:
    for attr, value in user_data.dict(exclude_unset=True).items():
        setattr(db_user, attr, value)
    db.commit()
    db.refresh(db_user)
  return db_user

def delete_user(db: Session, user_id: int):
  db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
  if db_user:
    db_user.deleted_at = datetime.now(UTC)
    db.commit()
  return db_user
