from fastapi.testclient import TestClient
from pytest import fixture

from budgeapp import app


@fixture
def client():
    return TestClient(app)
