from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List 
from api.crud.shelter import get_shelters, get_shelter, create_shelter  # インポート修正
from api import schemas
from api.database import get_db

router = APIRouter(
    prefix="/shelters",
    tags=["shelters"],
)

@router.get("/", response_model=List[schemas.Shelter])
def read_shelters(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_shelters(db, skip=skip, limit=limit)

@router.get("/{shelter_id}", response_model=schemas.Shelter)
def read_shelter(shelter_id: int, db: Session = Depends(get_db)):
    shelter = get_shelter(db, shelter_id=shelter_id)
    if not shelter:
        raise HTTPException(status_code=404, detail="Shelter not found")
    return shelter

@router.post("/", response_model=schemas.Shelter)
def create_shelter(shelter: schemas.ShelterCreate, db: Session = Depends(get_db)):
    return create_shelter(db=db, shelter=shelter)
