from fastapi import APIRouter, Depends, HTTPException
from infrastructure.jwt.jwt_tokens import create_token
from infrastructure.database.user_repository import UserRepositoryImple
from use_case.user_use_case import Uses_Cases
from schemas.users_schemas import UsersSchemaLogin
from infrastructure.database.dependency import get_db

router = APIRouter()


@router.post("/login")
def Login(user: UsersSchemaLogin, db=Depends(get_db)):
    repo = UserRepositoryImple(db)
    uses_cases = Uses_Cases(repo)

    token = uses_cases.Auth(user)
    return {"access_token": token, "token_type": "bearer"}
