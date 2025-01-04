from pydantic import SecretStr
from pytest import fixture, raises

from budgeapp.models.password import PasswordHash
from budgeapp.models.user import UserCreate


@fixture
def user_create():
    return UserCreate(
        email="test@example.com",
        password=SecretStr("password"),
        password_confirmation=SecretStr("password"),
    )


def test_user_create_password_hash(user_create):
    assert isinstance(user_create.password_hash, PasswordHash)


def test_user_create_validate_password_confirmation(user_create):
    assert user_create._validate_password_confirmation() == user_create


def test_user_create_validate_password_confirmation_raises(user_create):
    user_create.password_confirmation = SecretStr("wrong")

    with raises(ValueError, match="password and password_confirmation do not match"):
        user_create._validate_password_confirmation()
