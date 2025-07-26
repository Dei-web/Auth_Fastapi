from jose import jwt
from jose.exceptions import JWTError
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from passlib.context import CryptContext

SECRET_KEY = os.getenv("SECRET_KEY")


def create_token(data: dict, expires_minutes=30):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, str(SECRET_KEY), algorithm="HS256")


def verify_token(token: str):
    try:
        return jwt.decode(token, str(SECRET_KEY), algorithms=["HS256"])
    except JWTError:
        return None


# Crea el contexto para bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Verificar si la contraseña ingresada coincide con la hasheada
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# También puedes tener una función para hashear
def hash_password(password: str) -> str:
    return pwd_context.hash(password)
