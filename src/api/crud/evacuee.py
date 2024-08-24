from sqlalchemy.orm import Session
from api import models, schemas

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
