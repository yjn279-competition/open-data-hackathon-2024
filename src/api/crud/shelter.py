from sqlalchemy.orm import Session
from api import models, schemas

"""
データベースから複数の避難所を取得します。取得範囲を指定するためのskipとlimit引数を取ります。
"""
def get_shelters(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Shelter).offset(skip).limit(limit).all()

"""
特定の避難所をshelter_codeで取得します。存在しない場合はNoneを返します。
"""
def get_shelter(db: Session, shelter_code: str):
    return db.query(models.Shelter).filter(models.Shelter.shelter_code == shelter_code).first()

"""
新しい避難所をデータベースに追加します。
"""
def create_shelter(db: Session, shelter: schemas.ShelterCreate):
    db_shelter = models.Shelter(**shelter.dict())
    db.add(db_shelter)
    db.commit()
    db.refresh(db_shelter)
    return db_shelter

"""
既存の避難所を更新します。更新するフィールドのみを指定します。
"""
def update_shelter(db: Session, shelter_code: str, shelter_update: schemas.ShelterUpdate):
    db_shelter = db.query(models.Shelter).filter(models.Shelter.shelter_code == shelter_code).first()
    if db_shelter:
        for key, value in shelter_update.dict(exclude_unset=True).items():
            setattr(db_shelter, key, value)
        db.commit()
        db.refresh(db_shelter)
    return db_shelter

"""
特定の避難所を削除します。存在しない場合はNoneを返します。
"""
def delete_shelter(db: Session, shelter_code: str):
    db_shelter = db.query(models.Shelter).filter(models.Shelter.shelter_code == shelter_code).first()
    if db_shelter:
        db.delete(db_shelter)
        db.commit()
    return db_shelter
