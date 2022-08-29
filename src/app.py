from fastapi import FastAPI

from api import router
from project.settings import settings

app = FastAPI(
    title=settings.title,
    description=settings.description,
    version='1.0.0',
)
app.include_router(router)
