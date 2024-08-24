from sqlalchemy.orm import Session
from api import models, schemas

def get_materials(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Material).offset(skip).limit(limit).all()

def get_material(db: Session, material_id: int):
    return db.query(models.Material).filter(models.Material.id == material_id).first()

def create_material(db: Session, material: schemas.MaterialCreate):
    db_material = models.Material(name=material.name, quantity=material.quantity)
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    
    for detail in material.details:
        db_detail = models.MaterialDetail(material_id=db_material.id, **detail.dict())
        db.add(db_detail)
    
    db.commit()
    return db_material
