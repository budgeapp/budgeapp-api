import uuid
from datetime import datetime, timezone

from sqlalchemy import DateTime
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column


def now():
    return datetime.now(timezone.utc)


class BaseModel(MappedAsDataclass, AsyncAttrs, DeclarativeBase):
    id: Mapped[uuid.UUID] = mapped_column(default_factory=uuid.uuid4, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default_factory=now
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default_factory=now, onupdate=now
    )
