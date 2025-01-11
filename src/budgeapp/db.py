from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from budgeapp.env import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True)
async_factory = async_sessionmaker(engine, expire_on_commit=False)


async def _async_session():
    async with async_factory() as session:
        yield session


async_session = asynccontextmanager(_async_session)

AsyncSessionDep = Annotated[AsyncSession, Depends(_async_session)]
