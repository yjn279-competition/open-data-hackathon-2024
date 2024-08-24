from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List  # インポート修正
from api.crud.material import get_materials, get_material, create_material  # インポート修正
from api import schemas
from api.database import get_db

router = APIRouter(
    prefix="/materials",
    tags=["materials"],
)

@router.get("/", response_model=List[schemas.Material])
def read_materials(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_materials(db, skip=skip, limit=limit)

@router.get("/{material_id}", response_model=schemas.Material)
def read_material(material_id: int, db: Session = Depends(get_db)):
    material = get_material(db, material_id=material_id)
    if not material:
        raise HTTPException(status_code=404, detail="Material not found")
    return material

@router.post("/", response_model=schemas.Material)
def create_material(material: schemas.MaterialCreate, db: Session = Depends(get_db)):
    return create_material(db=db, material=material)
