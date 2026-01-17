from sqlalchemy.orm import Session
from app.models import User
from app.auth import hash_password

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_name(db: Session, name: str):
    return db.query(User).filter(User.name == name).first()

def create_user(db: Session, user_data):
    db_user = User(
        name=user_data.name,
        website=user_data.website,
        age=user_data.age,
        role=user_data.role,
        password_hash=hash_password(user_data.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, db_user, update_data):
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, db_user):
    db.delete(db_user)
    db.commit()