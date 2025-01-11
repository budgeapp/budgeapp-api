from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from budgeapp.db import AsyncSessionDep
from budgeapp.models import Token, User

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(path="password")
async def password_auth(
    auth: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: AsyncSessionDep,
) -> Token:
    user = await User.authenticate(auth, db)

    if user is not None:
        return Token.for_user(user)

    raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED)
