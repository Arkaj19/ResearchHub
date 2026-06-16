"""
services/research_service.py
-----------------------------
Business logic for the Research domain.
Service functions are called by route handlers and interact
directly with the database. No HTTP concerns live here.
"""

from typing import List
import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.db_models import ResearchJob
from models.research_model import TaskStatus


# ---------------------------------------------------------------------------
# Create
# ---------------------------------------------------------------------------

async def create_research_job(query: str, db: AsyncSession) -> ResearchJob:
    """
    Creates a new research job in the database with status Pending.

    Args:
        query: The user's research query string.
        db:    The async database session (injected via Depends).

    Returns:
        The newly created ResearchJob ORM object.
    """
    job = ResearchJob(
        query=query,
        status=TaskStatus.PENDING,
    )

    db.add(job)
    await db.commit()
    await db.refresh(job)   # re-fetches the row so created_at etc. are populated

    return job


# ---------------------------------------------------------------------------
# Read
# ---------------------------------------------------------------------------

async def get_researchjob_by_id(job_id: str, db: AsyncSession) -> ResearchJob | None:
    """
    Fetches a single research job by its UUID.

    Args:
        job_id: String representation of the job's UUID.
        db:     The async database session (injected via Depends).

    Returns:
        The matching ResearchJob ORM object, or None if not found.
    """
    stmt = select(ResearchJob).where(ResearchJob.id == uuid.UUID(job_id))
    result = await db.execute(stmt)

    return result.scalar_one_or_none()


async def get_all_research_jobs(db : AsyncSession)-> List[ResearchJob]:
    
    query = select(ResearchJob).order_by(ResearchJob.created_at.desc())
    result = await db.execute(query)

    return result.scalars().all()