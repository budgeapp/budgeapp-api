from http import HTTPStatus
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from sqlalchemy.exc import NoResultFound

from budgeapp.db import AsyncDbSession
from budgeapp.models import Token, User

oauth2_password_scheme = OAuth2PasswordBearer("/auth/password")

BearerToken = Annotated[str, Depends(oauth2_password_scheme)]


async def _current_user(bearer: BearerToken, db: AsyncDbSession):
    try:
        token = Token.decode(bearer)
        return await db.get_one(User, token.claims.sub)
    except (jwt.InvalidTokenError, ValidationError, NoResultFound) as e:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, headers={"WWW-Authenticate": "Bearer"}
        ) from e


CurrentUser = Annotated[User, Depends(_current_user)]
