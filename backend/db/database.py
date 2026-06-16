"""
db/database.py
--------------
Database connection and session management.
Provides:
  - async SQLAlchemy engine connected to Supabase via the session pooler
  - async session factory used throughout the app
  - Base class that all ORM models inherit from
  - get_db dependency injected into FastAPI route handlers
"""

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from core.config import settings

# ---------------------------------------------------------------------------
# Engine
# ---------------------------------------------------------------------------

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,       # logs all SQL when DEBUG=True — useful locally
    pool_pre_ping=True,        # re-validates connections dropped by Supabase idle timeout
)

# ---------------------------------------------------------------------------
# Session factory
# ---------------------------------------------------------------------------

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,    # keeps ORM objects usable after commit
)


# ---------------------------------------------------------------------------
# Base class for ORM models
# ---------------------------------------------------------------------------

class Base(DeclarativeBase):
    pass


# ---------------------------------------------------------------------------
# FastAPI dependency
# ---------------------------------------------------------------------------

async def get_db():
    """
    Yields an async database session for use in route handlers.
    The session is automatically closed when the request completes.

    Usage:
        @router.get("/example")
        async def example(db: AsyncSession = Depends(get_db)):
            ...
    """
    async with AsyncSessionLocal() as session:
        yield session