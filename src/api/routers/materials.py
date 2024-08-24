from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from api.crud.material import get_materials, get_material, create_material, update_material, delete_material
from api import schemas
from api.database import get_db

"""
Materialエンドポイントに関連するルーターを定義します。
"""
router = APIRouter(
    prefix="/materials",
    tags=["materials"],
)

"""
複数の材料を取得するエンドポイント。
"""
@router.get("/", response_model=List[schemas.Material])
def read_materials(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_materials(db, skip=skip, limit=limit)

"""
特定の材料を取得するエンドポイント。
"""
@router.get("/{material_id}", response_model=schemas.Material)
def read_material(material_id: str, db: Session = Depends(get_db)):
    material = get_material(db, material_id=material_id)
    if not material:
        raise HTTPException(status_code=404, detail="Material not found")
    return material

"""
新しい材料を作成するエンドポイント。
"""
@router.post("/", response_model=schemas.Material)
def create_material(material: schemas.MaterialCreate, db: Session = Depends(get_db)):
    return create_material(db=db, material=material)

"""
既存の材料を更新するエンドポイント。
"""
@router.put("/{material_id}", response_model=schemas.Material)
def update_material(material_id: str, material_update: schemas.MaterialUpdate, db: Session = Depends(get_db)):
    material = update_material(db=db, material_id=material_id, material_update=material_update)
    if not material:
        raise HTTPException(status_code=404, detail="Material not found")
    return material

"""
特定の材料を削除するエンドポイント。
"""
@router.delete("/{material_id}", response_model=schemas.Material)
def delete_material(material_id: str, db: Session = Depends(get_db)):
    material = delete_material(db=db, material_id=material_id)
    if not material:
        raise HTTPException(status_code=404, detail="Material not found")
    return material
