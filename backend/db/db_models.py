"""
db/db_models.py
---------------
SQLAlchemy ORM table definitions.
Each class maps to a physical table in PostgreSQL.
This file must be imported in main.py so that Base.metadata
is populated before create_all is called on startup.
"""

import uuid

from sqlalchemy import Column, DateTime, String, Text, func
from sqlalchemy.dialects.postgresql import UUID

from db.database import Base


class ResearchJob(Base):
    """
    Represents a single research job submitted by a user.

    Columns:
        id            -- UUID primary key, auto-generated
        query         -- the user's original research query
        status        -- current job state (Pending / Running / Completed / Failed)
        created_at    -- timestamp when the job was created
        updated_at    -- timestamp of the last status update
        result        -- final report text, populated when status = Completed
        error_message -- failure reason, populated when status = Failed
    """

    __tablename__ = "research_jobs"

    # ---- Identity ----
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
    )

    # ---- Payload ----
    query = Column(Text, nullable=False)
    status = Column(String(20), nullable=False, default="Pending")

    # ---- Timestamps ----
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # ---- Output ----
    result = Column(Text, nullable=True)
    error_message = Column(Text, nullable=True)