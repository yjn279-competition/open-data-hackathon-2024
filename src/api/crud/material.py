from sqlalchemy.orm import Session
from api import models, schemas

def get_materials(db: Session, skip: int = 0, limit: int = 10):
    """
    複数の材料を取得する関数

    Args:
        db (Session): データベースセッション。
        skip (int): スキップするレコードの数。デフォルトは0。
        limit (int): 取得するレコードの上限。デフォルトは10。

    Returns:
        List[models.Material]: 材料情報のリスト。
    """
    return db.query(models.Material).offset(skip).limit(limit).all()

def get_material(db: Session, material_id: str):
    """
    特定の材料をIDで取得する関数

    Args:
        db (Session): データベースセッション。
        material_id (str): 取得する材料のID。

    Returns:
        models.Material: 指定したIDの材料情報。見つからない場合はNoneを返す。
    """
    return db.query(models.Material).filter(models.Material.material_id == material_id).first()

def create_material(db: Session, material: schemas.MaterialCreate):
    """
    新しい材料を作成する関数

    Args:
        db (Session): データベースセッション。
        material (schemas.MaterialCreate): 作成する材料情報のデータ。

    Returns:
        models.Material: 作成された材料情報。
    """
    db_material = models.Material(**material.dict())
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

def update_material(db: Session, material_id: str, material_update: schemas.MaterialUpdate):
    """
    既存の材料を更新する関数

    Args:
        db (Session): データベースセッション。
        material_id (str): 更新する材料のID。
        material_update (schemas.MaterialUpdate): 更新するデータ。

    Returns:
        models.Material: 更新された材料情報。見つからない場合はNoneを返す。
    """
    db_material = db.query(models.Material).filter(models.Material.material_id == material_id).first()
    if db_material:
        for key, value in material_update.dict(exclude_unset=True).items():
            setattr(db_material, key, value)
        db.commit()
        db.refresh(db_material)
    return db_material

def delete_material(db: Session, material_id: str):
    """
    特定の材料を削除する関数

    Args:
        db (Session): データベースセッション。
        material_id (str): 削除する材料のID。

    Returns:
        models.Material: 削除された材料情報。見つからない場合はNoneを返す。
    """
    db_material = db.query(models.Material).filter(models.Material.material_id == material_id).first()
    if db_material:
        db.delete(db_material)
        db.commit()
    return db_material
