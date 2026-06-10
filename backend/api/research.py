from fastapi import APIRouter
from models.research_model import TaskStatus,QueryResponse,ResearchQuery
from services.research_service import gen_research_job

router = APIRouter()

@router.get("/")
def hello():
    return "Hello, this is the New Backend Project"

@router.post("/research", response_model=QueryResponse)
def create_research_job(query: ResearchQuery):

    job_id = gen_research_job()

    return QueryResponse(
        job_id=job_id,
        status=TaskStatus.RUNNING
    )
