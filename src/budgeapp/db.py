from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from .env import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True)
_factory = async_sessionmaker(engine, expire_on_commit=False)
session = _factory()


async def async_session():  # pragma: no cover
    async with session.begin():
        yield session


AsyncDbSession = Annotated[AsyncSession, Depends(async_session)]
