from sqlalchemy.orm import Mapped, mapped_column

from budgeapp.models.base import BaseModel


class UserModel(BaseModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True, kw_only=True)
