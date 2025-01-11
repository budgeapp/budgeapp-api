from httpx import ASGITransport, AsyncClient
from pytest import fixture

from budgeapp import app


@fixture
async def client():
    return AsyncClient(transport=ASGITransport(app=app), base_url="http://test")
