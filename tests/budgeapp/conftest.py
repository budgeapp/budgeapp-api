from contextlib import asynccontextmanager

from faker import Faker
from pytest import fixture

from budgeapp.db import async_session
from budgeapp.models.password import PasswordHash
from budgeapp.models.user import User


@fixture
def faker() -> Faker:
    return Faker()


@fixture
async def user_factory(faker):
    async def _user_factory(password: str = faker.password()):
        user = User(email=faker.email(), password_hash=PasswordHash(password))

        async with async_session() as db:
            db.add(user)
            await db.commit()

            yield user

            await db.delete(user)

    return asynccontextmanager(_user_factory)
