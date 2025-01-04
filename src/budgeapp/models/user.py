import uuid

from pydantic import EmailStr, SecretStr, computed_field, model_validator
from sqlmodel import Field, SQLModel

from .password import PasswordField, PasswordHash


class UserBase(SQLModel):
    email: EmailStr = Field(unique=True)


class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    password_hash: PasswordField


class UserCreate(UserBase):
    password: SecretStr
    password_confirmation: SecretStr

    @computed_field
    def password_hash(self) -> PasswordHash:
        return PasswordHash(self.password.get_secret_value())

    @model_validator(mode="after")
    def _validate_password_confirmation(self):
        if self.password != self.password_confirmation:
            raise ValueError("password and password_confirmation do not match")

        return self
