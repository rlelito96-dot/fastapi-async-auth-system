# Imports
from app.database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


# Models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    website = Column(String)
    age = Column(Integer)
    role = Column(String)
    password_hash = Column(String, nullable=False)
