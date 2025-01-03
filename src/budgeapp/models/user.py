import uuid

from pydantic import EmailStr
from sqlmodel import Field, SQLModel

from .password import PasswordField


class UserBase(SQLModel):
    email: EmailStr = Field(unique=True)


class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    password_hash: PasswordField
