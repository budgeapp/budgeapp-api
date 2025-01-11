from argon2 import PasswordHasher
from pytest import fixture, raises

from budgeapp.models.password import Password, PasswordHash


@fixture
def hasher():
    return PasswordHasher()


def test_password_hash_from_password(hasher):
    _hash = PasswordHash("password")
    assert hasher.verify(_hash.get_secret_value(), "password")


def test_password_hash_from_hash(hasher):
    hashed_password = hasher.hash("password")
    _hash = PasswordHash(hashed_password)
    assert hasher.verify(_hash.get_secret_value(), "password")


def test_password_hash_eq_str():
    _hash = PasswordHash("password")
    assert _hash == "password"
    assert _hash != "not password"


def test_password_hash_eq_password_hash():
    _hash1 = PasswordHash("password")
    _hash2 = _hash1
    assert _hash1 == _hash2

    _hash3 = PasswordHash("not password")
    assert _hash1 != _hash3


@fixture
def password_column():
    return Password()


def test_password_process_bind_param_with_str(password_column, hasher):
    assert hasher.verify(
        password_column.process_bind_param("password", None), "password"
    )


def test_password_process_bind_param_with_password_hash(password_column, hasher):
    _hash = PasswordHash("password")
    assert hasher.verify(password_column.process_bind_param(_hash, None), "password")


def test_password_process_result_value_with_str(password_column):
    assert password_column.process_result_value("password", None) == "password"


def test_password_process_result_value_with_password_hash(password_column):
    _hash = PasswordHash("password")
    assert password_column.process_result_value(_hash, None) == "password"


def test_password_confirm_with_invalid_type(password_column):
    with raises(TypeError):
        password_column._convert(1)
