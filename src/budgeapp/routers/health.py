from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from sqlmodel import select, text

from budgeapp.db import AsyncSessionDep

router = APIRouter(prefix="/health", tags=["health"])


@router.get("", response_class=PlainTextResponse)
async def health_check(db: AsyncSessionDep):
    return await db.scalar(select(text("'ok'")))
