import pytest


@pytest.mark.asyncio
async def test_auth_password(client, user_factory):
    user, password = user_factory
    response = await client.post(
        "/auth/password", data={"username": user.email, "password": password}
    )
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_auth_password_incorrect_email(faker, client, user_factory):
    _, password = user_factory
    response = await client.post(
        "/auth/password", data={"username": faker.email(), "password": password}
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_auth_password_incorrect_password(faker, client, user_factory):
    user, _ = user_factory
    response = await client.post(
        "/auth/password", data={"username": user.email, "password": faker.password()}
    )
    assert response.status_code == 401
