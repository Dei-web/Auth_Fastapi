from app.domain.entities.port.users_repository import User_repository
from app.infrastructure.jwt.jwt_tokens import create_token, verify_password
from app.schemas.users_schemas import (
    UsersSchema,
    UsersSchemaCreate,
    UsersSchemaLogin,
    UsersSchemaUpdate,
)


class Uses_Cases:
    def __init__(self, User_repo: User_repository):
        self.User_repo = User_repo

    def create(self, Users_data: UsersSchemaCreate) -> UsersSchema:
        return self.User_repo.create(Users_data)

    def Update(self, Users_data: UsersSchemaUpdate) -> UsersSchema:
        return self.User_repo.update_user(Users_data)

    def Auth(self, Users_data: UsersSchemaLogin) -> str:
        Users = self.User_repo.get_by_email(Users_data)
        if not Users or not verify_password(Users_data.password, str(Users.password)):
            raise ValueError("Invalid credentials")

        token = create_token({"sub": Users.email})
        return token
