from sqlalchemy.orm import Session
from api import models, schemas

# Evacuee
def get_evacuees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Evacuee).offset(skip).limit(limit).all()

def get_evacuee(db: Session, evacuee_id: int):
    return db.query(models.Evacuee).filter(models.Evacuee.id == evacuee_id).first()

def create_evacuee(db: Session, evacuee: schemas.EvacueeCreate):
    db_evacuee = models.Evacuee(**evacuee.dict())
    db.add(db_evacuee)
    db.commit()
    db.refresh(db_evacuee)
    return db_evacuee

# Material
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

# MaterialDetail
def get_material_detail(db: Session, detail_id: int):
    return db.query(models.MaterialDetail).filter(models.MaterialDetail.id == detail_id).first()

def create_material_detail(db: Session, detail: schemas.MaterialDetailCreate, material_id: int):
    db_detail = models.MaterialDetail(**detail.dict(), material_id=material_id)
    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)
    return db_detail
