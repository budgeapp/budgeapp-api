from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from sqlmodel import select

from budgeapp.db import AsyncSessionDep

router = APIRouter(prefix="/health", tags=["health"])


@router.get("", response_class=PlainTextResponse)
async def health_check(db: AsyncSessionDep):
    await db.execute(select(1))
    return "ok"
