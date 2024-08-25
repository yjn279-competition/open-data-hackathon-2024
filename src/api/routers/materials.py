from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from api.crud.material import get_materials, get_material, create_material, update_material, delete_material
from api import schemas
from api.database import get_db

# Materialエンドポイントに関連するルーターを定義
router = APIRouter(
    prefix="/materials",  # すべてのエンドポイントに適用される共通のURLプレフィックス
    tags=["materials"],   # ドキュメントで使用されるタグ
)

@router.get("/", response_model=List[schemas.Material])
def read_materials(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    複数の材料を取得するエンドポイント

    Args:
        skip (int): スキップするレコードの数。デフォルトは0。
        limit (int): 取得するレコードの上限。デフォルトは10。
        db (Session): データベースセッション。FastAPIの依存関係として注入される。

    Returns:
        List[schemas.Material]: 材料情報のリスト。
    """
    return get_materials(db, skip=skip, limit=limit)

@router.get("/{material_id}", response_model=schemas.Material)
def read_material(material_id: str, db: Session = Depends(get_db)):
    """
    特定の材料を取得するエンドポイント

    Args:
        material_id (str): 取得する材料のID。
        db (Session): データベースセッション。FastAPIの依存関係として注入される。

    Returns:
        schemas.Material: 指定したIDの材料情報。見つからない場合は404エラーを返す。
    """
    material = get_material(db, material_id=material_id)
    if not material:
        raise HTTPException(status_code=404, detail="Material not found")
    return material

@router.post("/", response_model=schemas.Material)
def create_material(material: schemas.MaterialCreate, db: Session = Depends(get_db)):
    """
    新しい材料を作成するエンドポイント

    Args:
        material (schemas.MaterialCreate): 作成する材料情報のデータ。
        db (Session): データベースセッション。FastAPIの依存関係として注入される。

    Returns:
        schemas.Material: 作成された材料情報。
    """
    return create_material(db=db, material=material)

@router.put("/{material_id}", response_model=schemas.Material)
def update_material(material_id: str, material_update: schemas.MaterialUpdate, db: Session = Depends(get_db)):
    """
    既存の材料を更新するエンドポイント

    Args:
        material_id (str): 更新する材料のID。
        material_update (schemas.MaterialUpdate): 更新する材料情報のデータ。
        db (Session): データベースセッション。FastAPIの依存関係として注入される。

    Returns:
        schemas.Material: 更新された材料情報。見つからない場合は404エラーを返す。
    """
    material = update_material(db=db, material_id=material_id, material_update=material_update)
    if not material:
        raise HTTPException(status_code=404, detail="Material not found")
    return material

@router.delete("/{material_id}", response_model=schemas.Material)
def delete_material(material_id: str, db: Session = Depends(get_db)):
    """
    特定の材料を削除するエンドポイント

    Args:
        material_id (str): 削除する材料のID。
        db (Session): データベースセッション。FastAPIの依存関係として注入される。

    Returns:
        schemas.Material: 削除された材料情報。見つからない場合は404エラーを返す。
    """
    material = delete_material(db=db, material_id=material_id)
    if not material:
        raise HTTPException(status_code=404, detail="Material not found")
    return material
