import uuid
from dataclasses import dataclass, field

import sqlalchemy as sa

from ._registry import registry


@registry.mapped
@dataclass
class User:
    __table__ = sa.Table(
        "users",
        registry.metadata,
        sa.Column("id", sa.UUID, primary_key=True),
    )

    id: uuid.UUID = field(default_factory=uuid.uuid4, init=False)
