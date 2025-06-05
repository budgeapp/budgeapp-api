import uuid
import pytest

from budgeapp.models.token import Token, TokenClaims

@pytest.mark.asyncio
async def test_create_user(faker, client):
    email = faker.email()
    password = faker.password()

    data = {"email": email, "password": password, "password_confirmation": password}

    response = await client.post("/user", json=data)
    assert response.status_code == 201

    response = await client.post("/user", json=data)
    assert response.status_code == 409


@pytest.mark.asyncio
async def test_get_user(client, user_factory):
    user, _ = user_factory
    token = Token.for_user(user)

    response = await client.get("/user", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == {
        "id": str(user.id),
        "email": user.email,
    }


@pytest.mark.asyncio
async def test_get_user_invalid_token(client):
    token = Token(claims=TokenClaims(sub=uuid.uuid4()))

    response = await client.get("/user", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 401
    assert response.headers["WWW-Authenticate"] == "Bearer"
