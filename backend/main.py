from fastapi import FastAPI

## Importing routers from varuous other files
from backend.api.research import router as research_router

app = FastAPI()

app.include_router(research_router)
