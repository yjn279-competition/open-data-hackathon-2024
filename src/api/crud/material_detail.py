from sqlalchemy.orm import Session
from api import models, schemas

# 複数の材料詳細を取得します
def get_material_details(db: Session, skip: int = 0, limit: int = 10):
    """
    複数の材料詳細を取得する関数

    Args:
        db (Session): データベースセッション。
        skip (int): スキップするレコードの数。デフォルトは0。
        limit (int): 取得するレコードの上限。デフォルトは10。

    Returns:
        List[models.MaterialDetail]: 材料詳細情報のリスト。
    """
    return db.query(models.MaterialDetail).offset(skip).limit(limit).all()

# 特定の材料詳細を取得します
def get_material_detail(db: Session, material_id: str, branch_number: str):
    """
    特定の材料詳細をIDと枝番号で取得する関数

    Args:
        db (Session): データベースセッション。
        material_id (str): 取得する材料のID。
        branch_number (str): 取得する材料の枝番号。

    Returns:
        models.MaterialDetail: 指定したIDと枝番号の材料詳細情報。見つからない場合はNoneを返す。
    """
    return db.query(models.MaterialDetail).filter(
        models.MaterialDetail.material_id == material_id, 
        models.MaterialDetail.branch_number == branch_number
    ).first()

# 新しい材料詳細を作成します
def create_material_detail(db: Session, detail: schemas.MaterialDetailCreate):
    """
    新しい材料詳細情報を作成する関数

    Args:
        db (Session): データベースセッション。
        detail (schemas.MaterialDetailCreate): 作成する材料詳細情報のデータ。

    Returns:
        models.MaterialDetail: 作成された材料詳細情報。
    """
    db_detail = models.MaterialDetail(**detail.dict())
    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)
    return db_detail

# 既存の材料詳細を更新します
def update_material_detail(db: Session, material_id: str, branch_number: str, detail_update: schemas.MaterialDetailUpdate):
    """
    既存の材料詳細情報を更新する関数

    Args:
        db (Session): データベースセッション。
        material_id (str): 更新する材料のID。
        branch_number (str): 更新する材料の枝番号。
        detail_update (schemas.MaterialDetailUpdate): 更新するデータ。

    Returns:
        models.MaterialDetail: 更新された材料詳細情報。見つからない場合はNoneを返す。
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
    """
    特定の材料詳細情報を削除する関数

    Args:
        db (Session): データベースセッション。
        material_id (str): 削除する材料のID。
        branch_number (str): 削除する材料の枝番号。

    Returns:
        models.MaterialDetail: 削除された材料詳細情報。見つからない場合はNoneを返す。
    """
    db_detail = get_material_detail(db, material_id, branch_number)  # 既存の材料詳細を取得
    if db_detail:
        db.delete(db_detail)
        db.commit()
    return db_detail
