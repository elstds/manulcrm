from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core.config import settings
from app.users import users_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan
)


app.include_router(users_router)
