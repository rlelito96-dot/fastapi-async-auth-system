# Imports
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

# Load .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Engine & session
engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

# FastAPI dependency
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
