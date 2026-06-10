from fastapi import APIRouter
from models.research_model import TaskStatus,QueryResponse,ResearchQuery

router = APIRouter()

@router.get("/")
def hello():
    return "Hello, this is the New Backend Project"

@router.post("/research", response_model=QueryResponse)
def create_research_job(query: ResearchQuery):
    return QueryResponse(
        job_id="ABC1234",
        status=TaskStatus.RUNNING
    )
