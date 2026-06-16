"""
api/research.py
---------------
Route handlers for the Research domain.
Handles HTTP concerns only — validation, status codes, and
response shaping. All business logic is delegated to the service layer.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_db
from models.research_model import QueryResponse, ResearchJobResponse, ResearchQuery, TaskStatus
from services.research_service import create_research_job, get_researchjob_by_id, get_all_research_jobs


router = APIRouter()


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------

@router.get("/", summary="Health check")
def hello():
    """Simple health check endpoint to confirm the API is running."""
    return {"message": "ResearchHub API is running"}


# ---------------------------------------------------------------------------
# Research jobs
# ---------------------------------------------------------------------------

@router.post(
    "/research",
    response_model=QueryResponse,
    status_code=201,
    summary="Create a research job",
)
async def create_research_job_endpoint(
    query: ResearchQuery,
    db: AsyncSession = Depends(get_db),
):
    """
    Accepts a research query, persists a new job in the database
    with status Pending, and returns the job ID for status polling.
    """
    job = await create_research_job(query.query, db)

    return QueryResponse(
        job_id=str(job.id),
        status=job.status,
    )


@router.get(
    "/research/{job_id}",
    response_model=ResearchJobResponse,
    summary="Get a research job by ID",
)
async def get_research_by_id(
    job_id: str,
    db: AsyncSession = Depends(get_db),
):
    """
    Returns the full details of a research job including its current
    status, result (if completed), and error message (if failed).

    Raises 404 if no job exists with the given ID.
    """
    job = await get_researchjob_by_id(job_id, db)

    if not job:
        raise HTTPException(status_code=404, detail=f"Job '{job_id}' not found")

    return job



@router.get("/research", response_model=list[ResearchJobResponse], summary="Get all research jobs")
async def get_all_research_jobs_endpoint( db:AsyncSession = Depends(get_db)):
        jobs = await get_all_research_jobs(db)
        return jobs