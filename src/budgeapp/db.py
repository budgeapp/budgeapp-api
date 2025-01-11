from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from budgeapp.env import DATABASE_URL

async_engine = create_async_engine(DATABASE_URL, echo=True)
_async_factory = async_sessionmaker(async_engine, expire_on_commit=False)


async def _async_session():
    async with _async_factory() as session:
        yield session


async_session = asynccontextmanager(_async_session)

AsyncSessionDep = Annotated[AsyncSession, Depends(_async_session)]
