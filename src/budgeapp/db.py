from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from budgeapp.env import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True)
_factory = async_sessionmaker(engine, expire_on_commit=False)
_async_session = _factory()


@asynccontextmanager
async def async_session():  # pragma: no cover
    yield _async_session


AsyncSessionDep = Annotated[AsyncSession, Depends(lambda: _async_session)]
