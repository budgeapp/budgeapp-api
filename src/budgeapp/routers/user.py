from fastapi import APIRouter

from ..auth import CurrentUser
from ..models import User

router = APIRouter(prefix="/user", tags=["user"])


@router.get("")
async def get_user(current_user: CurrentUser) -> User:
    return current_user
