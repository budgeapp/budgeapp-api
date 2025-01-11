import pytest


@pytest.mark.asyncio
async def test_auth_password(client, user_factory):
    user, password = user_factory
    response = await client.post(
        "/auth/password", data={"username": user.email, "password": password}
    )
    assert response.status_code == 200
