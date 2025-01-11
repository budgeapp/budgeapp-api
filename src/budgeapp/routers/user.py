from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError

from budgeapp.auth import CurrentUser
from budgeapp.db import AsyncSessionDep
from budgeapp.models import User
from budgeapp.models.user import UserCreate

router = APIRouter(prefix="/user", tags=["user"])


@router.post("", status_code=HTTPStatus.CREATED)
async def create_user(user_create: UserCreate, db: AsyncSessionDep) -> User:
    try:
        user = User.model_validate(user_create)
        db.add(user)
        await db.commit()
        return user
    except IntegrityError as e:
        raise HTTPException(status_code=HTTPStatus.CONFLICT) from e


@router.get("")
async def get_user(current_user: CurrentUser) -> User:
    return current_user
