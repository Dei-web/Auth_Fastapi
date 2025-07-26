import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import app
from app.infrastructure.database.config import SessionLocal
from app.infrastructure.database.models import Usermodel
from app.infrastructure.jwt.jwt_tokens import pwd_context
from app.schemas.users_schemas import UsersSchemaLogin

client = TestClient(app)


@pytest.fixture
def db_session():
    """Crea una sesión de DB temporal para cada test con rollback al final"""
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.rollback()
        db.close()


@pytest.fixture
def valid_user_data():
    return UsersSchemaLogin(name="alex", password="12345", email="polo").model_dump()


@pytest.fixture
def setup_test_user(db_session):
    """Inserta un usuario de prueba en la base de datos"""
    hashed_password = pwd_context.hash("12345")
    user = Usermodel(name="alex", email="polo", password=hashed_password)
    db_session.add(user)
    db_session.commit()


def test_login_success(valid_user_data, setup_test_user):
    response = client.post("/login", json=valid_user_data)
    print("response", response.json())
    assert response.status_code == 200
    assert "access_token" in response.json()
