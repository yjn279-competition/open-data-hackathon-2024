from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from api.crud.shelter import get_shelters, get_shelter, create_shelter, update_shelter, delete_shelter
from api import schemas
from api.database import get_db

"""
Shelterエンドポイントに関連するルーターを定義します。
"""
router = APIRouter(
    prefix="/shelters",
    tags=["shelters"],
)

"""
複数の避難所を取得するエンドポイント。
"""
@router.get("/", response_model=List[schemas.Shelter])
def read_shelters(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_shelters(db, skip=skip, limit=limit)

"""
特定の避難所を取得するエンドポイント。
"""
@router.get("/{shelter_code}", response_model=schemas.Shelter)
def read_shelter(shelter_code: str, db: Session = Depends(get_db)):
    shelter = get_shelter(db, shelter_code=shelter_code)
    if not shelter:
        raise HTTPException(status_code=404, detail="Shelter not found")
    return shelter

"""
新しい避難所を作成するエンドポイント。
"""
@router.post("/", response_model=schemas.Shelter)
def create_shelter(shelter: schemas.ShelterCreate, db: Session = Depends(get_db)):
    return create_shelter(db=db, shelter=shelter)

"""
既存の避難所を更新するエンドポイント。
"""
@router.put("/{shelter_code}", response_model=schemas.Shelter)
def update_shelter(shelter_code: str, shelter_update: schemas.ShelterUpdate, db: Session = Depends(get_db)):
    shelter = update_shelter(db=db, shelter_code=shelter_code, shelter_update=shelter_update)
    if not shelter:
        raise HTTPException(status_code=404, detail="Shelter not found")
    return shelter

"""
特定の避難所を削除するエンドポイント。
"""
@router.delete("/{shelter_code}", response_model=schemas.Shelter)
def delete_shelter(shelter_code: str, db: Session = Depends(get_db)):
    shelter = delete_shelter(db=db, shelter_code=shelter_code)
    if not shelter:
        raise HTTPException(status_code=404, detail="Shelter not found")
    return shelter
