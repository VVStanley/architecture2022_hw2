from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import db_Fight
from db.database import get_session

router = APIRouter(prefix='/fights', tags=['fights'])


@router.get("")
def get_fights(session: Session = Depends(get_session)):
    fights = session.query(db_Fight).all()
    return {
        "fights": fights
    }


@router.post("")
def add_fight(
    session: Session = Depends(get_session),
):
    a = 1
    return {"message": True}
