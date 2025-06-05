import uuid
from datetime import datetime, timedelta
from enum import StrEnum

import jwt
from pydantic import BaseModel, Field

from budgeapp import env
from budgeapp.models.user import User


def _expiry_time():
    return datetime.now() + timedelta(days=1)


class TokenType(StrEnum):
    BEARER = "Bearer"


class TokenClaims(BaseModel):
    jti: uuid.UUID = Field(default_factory=uuid.uuid4)
    exp: datetime = Field(default_factory=_expiry_time)
    sub: uuid.UUID

    def into_jwt(self):
        return {
            "jti": str(self.jti),
            "exp": int(self.exp.timestamp()),
            "sub": str(self.sub),
        }

class Token(BaseModel):
    claims: TokenClaims
    token_type: TokenType = TokenType.BEARER

    def __str__(self):
        return jwt.encode(
            self.claims.into_jwt(), env.JWT_SECRET, algorithm=env.JWT_ALGORITHM
        )

    @classmethod
    def decode(cls, token: str):
        claims = TokenClaims(
            **jwt.decode(token, env.JWT_SECRET, algorithms=[env.JWT_ALGORITHM])
        )

        return cls(claims=claims)

    @classmethod
    def for_user(cls, user: User):
        return cls(claims=TokenClaims(sub=user.id))
