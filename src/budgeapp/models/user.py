import uuid

from fastapi.security import OAuth2PasswordRequestForm
from pydantic import EmailStr, SecretStr, computed_field, model_validator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Field, SQLModel, select

from budgeapp.models.password import PasswordField, PasswordHash


class UserBase(SQLModel):
    email: EmailStr = Field(unique=True)


class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    password_hash: PasswordField

    @classmethod
    async def authenticate(cls, auth: OAuth2PasswordRequestForm, db: AsyncSession):
        query = select(cls).where(cls.email == auth.username)
        user = await db.scalar(query)

        if user is not None and user.password_hash == auth.password:
            return user


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
