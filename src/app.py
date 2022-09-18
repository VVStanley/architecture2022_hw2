from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api import router
from project.settings import settings

origins = ['*']

app = FastAPI(
    title=settings.title,
    description=settings.description,
    version='1.0.0',
)
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
