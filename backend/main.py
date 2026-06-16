"""
main.py
-------
Application entry point.
Initialises the FastAPI app, registers routers, and creates
database tables on startup.
"""

from fastapi import FastAPI

from api.research import router as research_router
from core.config import settings
from db import db_models                          # registers models with Base.metadata
from db.database import Base, engine


# ---------------------------------------------------------------------------
# App initialisation
# ---------------------------------------------------------------------------

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
)


# ---------------------------------------------------------------------------
# Routers
# ---------------------------------------------------------------------------

app.include_router(research_router, tags=["Research"])


# ---------------------------------------------------------------------------
# Startup event
# ---------------------------------------------------------------------------

# @app.on_event("startup")
# async def startup() -> None:
#     """Create all tables on startup if they do not already exist."""
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)