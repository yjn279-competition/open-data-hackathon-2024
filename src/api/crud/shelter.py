from sqlalchemy.orm import Session
from api import models, schemas

def get_shelters(db: Session, skip: int = 0, limit: int = 10):
    """
    複数の避難所を取得する関数

    Args:
        db (Session): データベースセッション。
        skip (int): スキップするレコードの数。デフォルトは0。
        limit (int): 取得するレコードの上限。デフォルトは10。

    Returns:
        List[models.Shelter]: 避難所情報のリスト。
    """
    return db.query(models.Shelter).offset(skip).limit(limit).all()

def get_shelter(db: Session, shelter_code: str):
    """
    特定の避難所をコードで取得する関数

    Args:
        db (Session): データベースセッション。
        shelter_code (str): 取得する避難所のコード。

    Returns:
        models.Shelter: 指定したコードの避難所情報。見つからない場合はNoneを返す。
    """
    return db.query(models.Shelter).filter(models.Shelter.shelter_code == shelter_code).first()

def create_shelter(db: Session, shelter: schemas.ShelterCreate):
    """
    新しい避難所を作成する関数

    Args:
        db (Session): データベースセッション。
        shelter (schemas.ShelterCreate): 作成する避難所情報のデータ。

    Returns:
        models.Shelter: 作成された避難所情報。
    """
    db_shelter = models.Shelter(**shelter.dict())
    db.add(db_shelter)
    db.commit()
    db.refresh(db_shelter)
    return db_shelter

def update_shelter(db: Session, shelter_code: str, shelter_update: schemas.ShelterUpdate):
    """
    既存の避難所を更新する関数

    Args:
        db (Session): データベースセッション。
        shelter_code (str): 更新する避難所のコード。
        shelter_update (schemas.ShelterUpdate): 更新するデータ。

    Returns:
        models.Shelter: 更新された避難所情報。見つからない場合はNoneを返す。
    """
    db_shelter = db.query(models.Shelter).filter(models.Shelter.shelter_code == shelter_code).first()
    if db_shelter:
        for key, value in shelter_update.dict(exclude_unset=True).items():
            setattr(db_shelter, key, value)
        db.commit()
        db.refresh(db_shelter)
    return db_shelter

def delete_shelter(db: Session, shelter_code: str):
    """
    特定の避難所を削除する関数

    Args:
        db (Session): データベースセッション。
        shelter_code (str): 削除する避難所のコード。

    Returns:
        models.Shelter: 削除された避難所情報。見つからない場合はNoneを返す。
    """
    db_shelter = db.query(models.Shelter).filter(models.Shelter.shelter_code == shelter_code).first()
    if db_shelter:
        db.delete(db_shelter)
        db.commit()
    return db_shelter
