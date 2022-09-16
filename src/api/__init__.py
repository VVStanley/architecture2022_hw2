from fastapi import APIRouter

from api.auth import router as auth_router
from api.fights import router as fights_router
from api.home import router as home_router
from api.ws import router as ws_router

router = APIRouter()

router.include_router(ws_router)
router.include_router(auth_router)
router.include_router(home_router)
router.include_router(fights_router)
