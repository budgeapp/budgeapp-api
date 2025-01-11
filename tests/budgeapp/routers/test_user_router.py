import pytest


@pytest.mark.asyncio
async def test_create_user(faker, client):
    email = faker.email()
    password = faker.password()

    data = {"email": email, "password": password, "password_confirmation": password}

    response = await client.post("/user", json=data)
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_create_user_conflict(faker, client, user_factory):
    user, _ = user_factory
    password = faker.password()

    data = {
        "email": user.email,
        "password": password,
        "password_confirmation": password,
    }

    response = await client.post("/user", json=data)
    assert response.status_code == 409
