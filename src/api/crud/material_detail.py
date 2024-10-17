from sqlalchemy.orm import Session
from api import models, schemas

# 複数の材料詳細を取得します
def get_material_details(db: Session, skip: int = 0, limit: int = 10):
    """複数の材料詳細を取得する関数
    """
    return db.query(models.MaterialDetail).offset(skip).limit(limit).all()

# 特定の材料詳細を取得します
def get_material_detail(db: Session, material_id: str, branch_number: str):
    """特定の材料詳細をIDと枝番号で取得する関数
    """
    return db.query(models.MaterialDetail).filter(
        models.MaterialDetail.material_id == material_id, 
        models.MaterialDetail.branch_number == branch_number
    ).first()

# 新しい材料詳細を作成します
def create_material_detail(db: Session, detail: schemas.MaterialDetailCreate):
    """新しい材料詳細情報を作成する関数
    """
    db_detail = models.MaterialDetail(**detail.dict())
    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)
    return db_detail

# 既存の材料詳細を更新します
def update_material_detail(db: Session, material_id: str, branch_number: str, detail_update: schemas.MaterialDetailUpdate):
    """既存の材料詳細情報を更新する関数
    """
    db_detail = get_material_detail(db, material_id, branch_number)  # 既存の材料詳細を取得
    if db_detail:
        for key, value in detail_update.dict(exclude_unset=True).items():
            setattr(db_detail, key, value)
        db.commit()
        db.refresh(db_detail)
    return db_detail

# 特定の材料詳細を削除します
def delete_material_detail(db: Session, material_id: str, branch_number: str):
    """特定の材料詳細情報を削除する関数
    """
    db_detail = get_material_detail(db, material_id, branch_number)  # 既存の材料詳細を取得
    if db_detail:
        db.delete(db_detail)
        db.commit()
    return db_detail
