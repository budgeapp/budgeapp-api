from typing import Annotated

from argon2 import PasswordHasher, extract_parameters
from argon2.exceptions import InvalidHashError, VerifyMismatchError
from pydantic import SecretStr
from sqlalchemy import TypeDecorator, Unicode
from sqlmodel import Field

_hasher = PasswordHasher()


class PasswordHash(SecretStr):
    def __init__(self, value: str):
        try:
            extract_parameters(value)
        except InvalidHashError:
            value = _hasher.hash(value)

        super().__init__(value)

    def __eq__(self, candidate: str):
        try:
            return _hasher.verify(self._secret_value, candidate)
        except VerifyMismatchError:
            return False


class Password(TypeDecorator):
    impl = Unicode

    def process_bind_param(self, value, dialect):
        return self._convert(value).get_secret_value() if value is not None else value

    def process_result_value(self, value, dialect):
        return self._convert(value) if value is not None else value

    def _convert(self, value: PasswordHash | str):
        if isinstance(value, PasswordHash):
            return value
        elif isinstance(value, str):
            return PasswordHash(value)
        else:
            raise TypeError(f"expected {PasswordHash} or {str}, got {type(value)}")


PasswordField = Annotated[
    PasswordHash | None,
    Field(sa_type=Password, nullable=True, exclude=True, default=None),
]
