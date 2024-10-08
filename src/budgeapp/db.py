import os
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

DATABASE_URL_ENVIRON_KEY = "DATABASE_URL"


def get_database_url():
    database_url = os.environ.get(DATABASE_URL_ENVIRON_KEY)
    if database_url is not None:
        return database_url

    raise RuntimeError(f"{DATABASE_URL_ENVIRON_KEY} is not defined")


async_engine = create_async_engine(get_database_url())
async_factory = async_sessionmaker(async_engine, expire_on_commit=False)


@asynccontextmanager
async def async_session():
    async with async_factory() as async_session:
        async with async_session.begin():
            yield async_session
