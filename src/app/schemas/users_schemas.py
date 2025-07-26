from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Generic, TypeVar

from sqlalchemy import true


T = TypeVar("T")


class UsersSchema(BaseModel):
    id: int
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class UsersSchemaCreate(BaseModel):
    name: str
    correo: str
    password: str


class UsersSchemaUpdate(UsersSchemaCreate):
    id: int
    model_config = {"from_attributes": True}

    __annotations__ = {
        k: Optional[v] for k, v in UsersSchemaCreate.__annotations__.items()
    }


class TokenPayload(BaseModel):
    sub: str
    # role: str


# queria hacer implementaciones de schemas por defecto pero perdia
# el modo de hacerlo como se deberia hacer incurria en malas practicas
# jeje deiler del pasado aqui si lo puedo usar jejjeje
class UsersSchemaLogin(BaseModel):
    name: str
    password: str
    email: str
    model_config = ConfigDict(
        {
            "json_schema_extra": {
                "examples": [
                    {"name": "Enter your Name", "password": "enter your password"}
                ]
            }
        }
    )


class UserDelete(BaseModel):
    id: int


class Response(BaseModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]


class Request(BaseModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestUsers(BaseModel):
    parameter: UsersSchema = Field(...)
