import uuid
from dataclasses import dataclass, field

from sqlalchemy import UUID, Column, Table
from sqlalchemy.orm import registry as _registry

registry = _registry()


@registry.mapped
@dataclass
class User:
    __table__ = Table("users", registry.metadata, Column("id", UUID, primary_key=True))

    id: uuid.UUID = field(default_factory=uuid.uuid4, init=False)
