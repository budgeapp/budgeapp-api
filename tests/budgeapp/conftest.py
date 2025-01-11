from faker import Faker
from pytest import fixture

from budgeapp.db import async_factory, engine
from budgeapp.models.password import PasswordHash
from budgeapp.models.user import User


@fixture
async def faker():
    return Faker()


@fixture
async def db():
    async with async_factory() as db:
        yield db
    await engine.dispose()


@fixture
async def user_factory(faker, db):
    password = faker.password()
    user = User(email=faker.email(), password_hash=PasswordHash(password))

    db.add(user)
    await db.commit()

    yield user, password

    await db.delete(user)
