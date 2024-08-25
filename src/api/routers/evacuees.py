from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from api.crud.evacuee import create_evacuee as crud_create_evacuee, get_evacuees, get_evacuee, get_evacuee_details
from api import schemas
from api.database import get_db

# APIRouterを初期化し、エンドポイントに関する設定を行う
router = APIRouter(
    prefix="/evacuees",  # すべてのエンドポイントに適用される共通のURLプレフィックス
    tags=["evacuees"],   # ドキュメントで使用されるタグ
)


@router.get("/")
def read_evacuees(db: Session = Depends(get_db)):
    evacuees = get_evacuee_details(db)
    if not evacuees:
        raise HTTPException(status_code=404, detail="No evacuee details found")
    return evacuees

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
