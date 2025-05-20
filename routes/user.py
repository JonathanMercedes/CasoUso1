from fastapi import APIRouter, Depends, HTTPException, Body
from sqlmodel import Session
from db.database import get_session
from models.user import User
from crud.user import (
    get_users,
)

router = APIRouter()

@router.get("/", response_model=list[User])
def read_all(session: Session = Depends(get_session)):
    try:
        return get_users(session)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")