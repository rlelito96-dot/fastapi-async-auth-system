import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db
from app.auth import get_current_user

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False},
                       )

TestingSessionLocal = sessionmaker(
    class_=AsyncSession,
    expire_on_commit= False,
    bind=engine
)

@pytest.fixture(scope="session", autouse=True)
async def create_test_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata_create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata_drop_all)

async def override_get_db():
    async with TestingSessionLocal() as db:
        yield db


async def override_get_current_user():
    return {"id": 1, "email": "test@example.com"}

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

@pytest.fixture()
def client():
    return TestClient(app)
