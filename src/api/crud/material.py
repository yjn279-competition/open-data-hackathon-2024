from sqlalchemy.orm import Session
from api import models, schemas

"""
データベースから複数の材料を取得します。取得範囲を指定するためのskipとlimit引数を取ります。
"""
def get_materials(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Material).offset(skip).limit(limit).all()

"""
特定の材料をmaterial_idで取得します。存在しない場合はNoneを返します。
"""
def get_material(db: Session, material_id: str):
    return db.query(models.Material).filter(models.Material.material_id == material_id).first()

"""
新しい材料をデータベースに追加します。
"""
def create_material(db: Session, material: schemas.MaterialCreate):
    db_material = models.Material(**material.dict())
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

"""
既存の材料を更新します。更新するフィールドのみを指定します。
"""
def update_material(db: Session, material_id: str, material_update: schemas.MaterialUpdate):
    db_material = db.query(models.Material).filter(models.Material.material_id == material_id).first()
    if db_material:
        for key, value in material_update.dict(exclude_unset=True).items():
            setattr(db_material, key, value)
        db.commit()
        db.refresh(db_material)
    return db_material

"""
特定の材料を削除します。存在しない場合はNoneを返します。
"""
def delete_material(db: Session, material_id: str):
    db_material = db.query(models.Material).filter(models.Material.material_id == material_id).first()
    if db_material:
        db.delete(db_material)
        db.commit()
    return db_material
