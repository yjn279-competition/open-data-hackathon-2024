from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.crud.evacuee import get_evacuees, get_evacuee, create_evacuee  # 修正部分
from typing import List
from api import schemas
from api.database import get_db

router = APIRouter(
    prefix="/evacuees",
    tags=["evacuees"],
)

@router.get("/", response_model=List[schemas.Evacuee])
def read_evacuees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_evacuees(db, skip=skip, limit=limit)

@router.get("/{evacuee_id}", response_model=schemas.Evacuee)
def read_evacuee(evacuee_id: int, db: Session = Depends(get_db)):
    evacuee = get_evacuee(db, evacuee_id=evacuee_id)
    if not evacuee:
        raise HTTPException(status_code=404, detail="Evacuee not found")
    return evacuee

@router.post("/", response_model=schemas.Evacuee)
def create_evacuee(evacuee: schemas.EvacueeCreate, db: Session = Depends(get_db)):
    return create_evacuee(db=db, evacuee=evacuee)
