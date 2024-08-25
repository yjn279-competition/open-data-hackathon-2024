from sqlalchemy.orm import Session
from api import models, schemas
from sqlalchemy import text
from fastapi.encoders import jsonable_encoder


def get_evacuee_details(db: Session):
    query = text("""
        SELECT
            card.full_name,
            card.birth_date,
            card.address,
            evacuee.is_safety,
            shelter.name AS shelter_name,
            shelter.address AS shelter_address
        FROM
            evacuee_table AS evacuee
            INNER JOIN my_number_card AS card ON evacuee.evacuee_id = card.card_number
            INNER JOIN shelter_table AS shelter ON evacuee.shelter_code = shelter.shelter_code;
    """)
    
    # 辞書形式で結果を取得
    result = db.execute(query)
    rows = result.mappings().all()

    response_content = [
        {
            "full_name": row['full_name'],
            "birth_date": row['birth_date'],
            "address": row['address'],
            "is_safety": row['is_safety'],
            "shelter_name": row['shelter_name'],
            "shelter_address": row['shelter_address']
        }
        for row in rows
    ]

    return response_content

def get_evacuees(db: Session, skip: int = 0, limit: int = 10):
    """
    複数の避難者情報を取得する関数

    Args:
        db (Session): データベースセッション。
        skip (int): スキップするレコードの数。デフォルトは0。
        limit (int): 取得するレコードの上限。デフォルトは10。

    Returns:
        List[models.Evacuee]: 避難者情報のリスト。
    """
    return db.query(models.Evacuee).offset(skip).limit(limit).all()

def get_evacuee(db: Session, evacuee_id: str):
    """
    特定の避難者情報をIDで取得する関数

    Args:
        db (Session): データベースセッション。
        evacuee_id (str): 取得する避難者のID。

    Returns:
        models.Evacuee: 避難者情報。見つからない場合はNoneを返す。
    """
    return db.query(models.Evacuee).filter(models.Evacuee.evacuee_id == evacuee_id).first()

def create_evacuee(db: Session, evacuee: schemas.EvacueeCreate):
    """
    新しい避難者情報を作成する関数

    Args:
        db (Session): データベースセッション。
        evacuee (schemas.EvacueeCreate): 作成する避難者情報のデータ。

    Returns:
        models.Evacuee: 作成された避難者情報。
    """
    db_evacuee = models.Evacuee(**evacuee.dict())
    db.add(db_evacuee)
    db.commit()
    db.refresh(db_evacuee)
    return db_evacuee

def update_evacuee(db: Session, evacuee_id: str, evacuee_update: schemas.EvacueeUpdate):
    """
    既存の避難者情報を更新する関数

    Args:
        db (Session): データベースセッション。
        evacuee_id (str): 更新する避難者のID。
        evacuee_update (schemas.EvacueeUpdate): 更新するデータ。

    Returns:
        models.Evacuee: 更新された避難者情報。見つからない場合はNoneを返す。
    """
    db_evacuee = db.query(models.Evacuee).filter(models.Evacuee.evacuee_id == evacuee_id).first()
    if db_evacuee:
        for key, value in evacuee_update.dict(exclude_unset=True).items():
            setattr(db_evacuee, key, value)
        db.commit()
        db.refresh(db_evacuee)
    return db_evacuee

def delete_evacuee(db: Session, evacuee_id: str):
    """
    特定の避難者情報を削除する関数

    Args:
        db (Session): データベースセッション。
        evacuee_id (str): 削除する避難者のID。

    Returns:
        models.Evacuee: 削除された避難者情報。見つからない場合はNoneを返す。
    """
    db_evacuee = db.query(models.Evacuee).filter(models.Evacuee.evacuee_id == evacuee_id).first()
    if db_evacuee:
        db.delete(db_evacuee)
        db.commit()
    return db_evacuee
