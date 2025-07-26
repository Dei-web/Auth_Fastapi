from sqlalchemy.orm import Session
from app.domain.entities.port.users_repository import User_repository
from app.schemas.users_schemas import (
    UsersSchema,
    UsersSchemaCreate,
    UsersSchemaUpdate,
    UsersSchemaLogin,
)
from .models import Usermodel


class UserRepositoryImple(User_repository):
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, Users: UsersSchemaCreate) -> UsersSchema:
        db_user = Usermodel(**Users.model_dump())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return UsersSchema.model_validate(db_user)

    def update_user(self, Users: UsersSchemaUpdate) -> UsersSchema:
        db_user = self.db.query(Usermodel).filter(Usermodel.id == Users.id).first()
        if not db_user:
            raise ValueError("Users not found")
        for field, value in Users.model_dump(exclude_unset=True).items():
            setattr(db_user, field, value)
        self.db.commit()
        self.db.refresh(db_user)
        return UsersSchema.model_validate(db_user)

    def get_by_email(self, Users: UsersSchemaLogin) -> UsersSchema | None:
        db_users = (
            self.db.query(Usermodel).filter(Usermodel.email == Users.email).first()
        )
        if db_users:
            return UsersSchema.model_validate(db_users)
        return None
