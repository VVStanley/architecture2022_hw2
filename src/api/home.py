from typing import Dict

from fastapi import APIRouter

router = APIRouter(prefix="", tags=["home"])


@router.get("/")
def home() -> Dict:
    return {"message": "Космический бой!!"}
