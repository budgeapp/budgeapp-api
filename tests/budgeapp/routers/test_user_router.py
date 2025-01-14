import pytest


@pytest.mark.asyncio
async def test_create_user(faker, client):
    email = faker.email()
    password = faker.password()

    data = {"email": email, "password": password, "password_confirmation": password}

    response = await client.post("/user", json=data)
    assert response.status_code == 201

    response = await client.post("/user", json=data)
    assert response.status_code == 409
