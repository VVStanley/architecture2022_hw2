from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api import router
from project.settings import settings

# origins = [
#     "http://localhost",
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
#     "http://localhost:8080",
#     'http://localhost:8080/',
#     "http://localhost:8999",
#     "http://localhost:8000",
#     "http://127.0.0.1:8080",
#     "http://127.0.0.1:8999",
#     "http://127.0.0.1:8000",
#    http://192.168.0.93:8080/
# ]
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
