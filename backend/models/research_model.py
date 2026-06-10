from pydantic import BaseModel
from typing import List,Optional,Dict
from enum import Enum

class ResearchQuery(BaseModel):
    query: str

class TaskStatus(str, Enum):
    PENDING = "Pending"
    RUNNING = "Running"
    COMPLETED = "Completed"
    FAILED = "Failed"

class QueryResponse(BaseModel):
    job_id: str
    status: TaskStatus

