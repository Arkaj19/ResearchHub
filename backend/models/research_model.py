"""
models/research_model.py
------------------------
Pydantic schemas for the Research domain.
These are the shapes of data that come IN (request bodies)
and go OUT (response bodies) through the API.
They are separate from the SQLAlchemy ORM models in db/db_models.py.
"""

import uuid
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class TaskStatus(str, Enum):
    """Possible states of a research job."""
    PENDING   = "Pending"
    RUNNING   = "Running"
    COMPLETED = "Completed"
    FAILED    = "Failed"


# ---------------------------------------------------------------------------
# Request schemas (inbound)
# ---------------------------------------------------------------------------

class ResearchQuery(BaseModel):
    """Body expected when creating a new research job."""
    query: str


# ---------------------------------------------------------------------------
# Response schemas (outbound)
# ---------------------------------------------------------------------------

class QueryResponse(BaseModel):
    """Returned immediately after a job is created (lightweight)."""
    job_id: str
    status: TaskStatus


class ResearchJobResponse(BaseModel):
    """
    Full job details returned by GET /research/{job_id}.
    Uses alias 'id' to map the SQLAlchemy column name to the
    API-friendly field name 'job_id'.
    """
    job_id: uuid.UUID = Field(alias="id")
    query: str
    status: TaskStatus
    result: Optional[str] = None
    error_message: Optional[str] = None

    class Config:
        from_attributes = True   # allows SQLAlchemy ORM objects to be passed directly
        populate_by_name = True  # allows both 'id' and 'job_id' to be used