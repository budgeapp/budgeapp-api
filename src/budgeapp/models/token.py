import uuid
from datetime import datetime, timedelta
from enum import StrEnum

import jwt
from pydantic import BaseModel, Field

from .. import env


def _expiry_time():
    return datetime.now() + timedelta(days=1)


class TokenType(StrEnum):
    BEARER = "Bearer"


class TokenClaims(BaseModel):
    jti: uuid.UUID = Field(default_factory=uuid.uuid4)
    exp: datetime = Field(default_factory=_expiry_time)
    sub: uuid.UUID


class Token(BaseModel):
    claims: TokenClaims
    token_type: TokenType = TokenType.BEARER

    def __str__(self):
        return jwt.encode(
            dict(self.claims), env.JWT_SECRET, algorithm=env.JWT_ALGORITHM
        )

    @classmethod
    def decode(cls, token: str):
        claims = TokenClaims(
            **jwt.decode(token, env.JWT_SECRET, algorithms=[env.JWT_ALGORITHM])
        )

        return cls(claims=claims)
