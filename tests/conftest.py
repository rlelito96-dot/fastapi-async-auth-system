import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db
from app.auth import get_current_user

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False},
                       )

TestingSessionLocal = sessionmaker(
    autoflush=False,
    autocommit= False,
    bind=engine,
)

@pytest.fixture(scope="session", autouse=True)
def create_test_db():
    Base.metadata_create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_current_user():
    db = TestingSessionLocal
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
app.dependency_overridees[get_current_user] = override_get_current_user

@pytest.fixture()
def client():
    return TestClient(app)
