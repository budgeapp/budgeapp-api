from importlib import metadata

import uvicorn
from fastapi import FastAPI

from budgeapp.routers import auth, health, user

distribution = metadata.distribution("budgeapp")

app = FastAPI(
    title="Budge API",
    version=distribution.version,
    description=distribution.metadata.get("summary", ""),
)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(health.router)


def main():  # pragma: no cover
    uvicorn.run(app, host="0.0.0.0", port=8000)
