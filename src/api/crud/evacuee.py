from sqlalchemy.orm import Session
from api import models, schemas

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
