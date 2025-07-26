from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.infrastructure.jwt.jwt_tokens import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_corrent_users(Token: str = Depends(oauth2_scheme)):
    payload = verify_token(Token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload
