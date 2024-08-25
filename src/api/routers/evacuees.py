from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from api.crud.evacuee import create_evacuee as crud_create_evacuee, get_evacuees, get_evacuee
from api import schemas
from api.database import get_db

# APIRouterを初期化し、エンドポイントに関する設定を行う
router = APIRouter(
    prefix="/evacuees",  # すべてのエンドポイントに適用される共通のURLプレフィックス
    tags=["evacuees"],   # ドキュメントで使用されるタグ
)

@router.get("/", response_model=List[schemas.Evacuee])
def read_evacuees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    複数の避難者情報を取得するエンドポイント

    Args:
        skip (int): スキップするレコードの数。デフォルトは0。
        limit (int): 取得するレコードの上限。デフォルトは10。
        db (Session): データベースセッション。FastAPIの依存関係として注入される。

    Returns:
        List[schemas.Evacuee]: 避難者情報のリスト。
    """
    return get_evacuees(db, skip=skip, limit=limit)

@router.get("/{evacuee_id}", response_model=schemas.Evacuee)
def read_evacuee(evacuee_id: str, db: Session = Depends(get_db)):
    """
    特定の避難者情報をIDで取得するエンドポイント

    Args:
        evacuee_id (str): 取得する避難者のID。
        db (Session): データベースセッション。FastAPIの依存関係として注入される。

    Returns:
        schemas.Evacuee: 指定したIDの避難者情報。見つからない場合は404エラーを返す。
    """
    evacuee = get_evacuee(db, evacuee_id=evacuee_id)
    if not evacuee:
        raise HTTPException(status_code=404, detail="Evacuee not found")
    return evacuee

@router.post("/", response_model=schemas.Evacuee)
def create_evacuee(evacuee: schemas.EvacueeCreate, db: Session = Depends(get_db)):
    """
    新しい避難者情報を作成するエンドポイント

    Args:
        evacuee (schemas.EvacueeCreate): 作成する避難者情報のデータ。
        db (Session): データベースセッション。FastAPIの依存関係として注入される。

    Returns:
        schemas.Evacuee: 作成された避難者情報。
    """
    return crud_create_evacuee(db=db, evacuee=evacuee)
