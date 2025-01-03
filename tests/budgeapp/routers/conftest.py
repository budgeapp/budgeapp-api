from unittest.mock import AsyncMock

from fastapi.testclient import TestClient
from pytest import fixture
from sqlalchemy.ext.asyncio import AsyncSession

from budgeapp import app


@fixture
def client():
    return TestClient(app)


_mock_db_session = AsyncMock(AsyncSession)
_mock_db_session.__aenter__.return_value = _mock_db_session
_mock_db_session.__aexit__ = AsyncMock()


@fixture
def mock_db_session():
    return _mock_db_session


async def mock_async_session():
    async with _mock_db_session as session:
        yield session
