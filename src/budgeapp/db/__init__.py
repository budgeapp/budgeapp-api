from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = "postgresql+asyncpg://budgeapp@localhost/budgeapp"

engine = create_async_engine(DATABASE_URL)
