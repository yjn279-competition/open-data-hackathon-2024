from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from api.crud.material_detail import get_material_details, get_material_detail, create_material_detail
from api import schemas
from api.database import get_db

# APIRouterを初期化し、エンドポイントに関する設定を行う
router = APIRouter(
    prefix="/material_details",  # すべてのエンドポイントに適用される共通のURLプレフィックス
    tags=["material_details"],   # ドキュメントで使用されるタグ
)



@router.get("/", response_model=List[schemas.MaterialDetail])
def read_material_details(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    複数の資材詳細情報を取得するエンドポイント

    Args:
        skip (int): スキップするレコードの数。デフォルトは0。
        limit (int): 取得するレコードの上限。デフォルトは10。
        db (Session): データベースセッション。FastAPIの依存関係として注入される。

    Returns:
        List[schemas.MaterialDetail]: 資材詳細情報のリスト。
    """
    return get_material_details(db, skip=skip, limit=limit)

@router.get("/{detail_id}", response_model=schemas.MaterialDetail)
def read_material_detail(detail_id: int, db: Session = Depends(get_db)):
    """
    特定の資材詳細情報をIDで取得するエンドポイント

    Args:
        detail_id (int): 取得する資材詳細のID。
        db (Session): データベースセッション。FastAPIの依存関係として注入される。

    Returns:
        schemas.MaterialDetail: 指定したIDの資材詳細情報。見つからない場合は404エラーを返す。
    """
    detail = get_material_detail(db, detail_id=detail_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Material Detail not found")
    return detail

@router.post("/", response_model=schemas.MaterialDetail)
def create_material_detail(detail: schemas.MaterialDetailCreate, db: Session = Depends(get_db)):
    """
    新しい資材詳細情報を作成するエンドポイント

    Args:
        detail (schemas.MaterialDetailCreate): 作成する資材詳細情報のデータ。
        db (Session): データベースセッション。FastAPIの依存関係として注入される。

    Returns:
        schemas.MaterialDetail: 作成された資材詳細情報。
    """
    return create_material_detail(db=db, detail=detail, material_id=detail.material_id)
