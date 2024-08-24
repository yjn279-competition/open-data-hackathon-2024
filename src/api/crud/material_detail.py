from sqlalchemy.orm import Session
from api import models, schemas

def get_material_details(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.MaterialDetail).offset(skip).limit(limit).all()

def get_material_detail(db: Session, detail_id: int):
    return db.query(models.MaterialDetail).filter(models.MaterialDetail.id == detail_id).first()

def create_material_detail(db: Session, detail: schemas.MaterialDetailCreate, material_id: int):
    db_detail = models.MaterialDetail(**detail.dict(), material_id=material_id)
    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)
    return db_detail
