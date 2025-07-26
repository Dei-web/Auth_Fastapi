from abc import ABC, abstractmethod
from schemas.users_schemas import (
    UsersSchema,
    UsersSchemaCreate,
    UsersSchemaUpdate,
    UsersSchemaLogin,
)


class User_repository(ABC):
    @abstractmethod
    def create(self, Users: UsersSchemaCreate) -> UsersSchema:
        pass

    @abstractmethod
    def update_user(self, Users: UsersSchemaUpdate) -> UsersSchema:
        pass

    @abstractmethod
    def get_by_email(self, Users: UsersSchemaLogin) -> UsersSchema | None:
        pass
