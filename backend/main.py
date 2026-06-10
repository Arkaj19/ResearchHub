from fastapi import FastAPI
from core.config import settings
from db.database import engine,Base
from db import db_models

## Importing routers from varuous other files
from api.research import router as research_router

app = FastAPI()

print(settings.APP_NAME)
print(settings.DEBUG)

app.include_router(research_router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

