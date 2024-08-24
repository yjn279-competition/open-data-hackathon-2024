from sqlalchemy.orm import Session
from api import models, schemas

def get_evacuees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Evacuee).offset(skip).limit(limit).all()

def get_evacuee(db: Session, evacuee_id: str):
    return db.query(models.Evacuee).filter(models.Evacuee.evacuee_id == evacuee_id).first()

def create_evacuee(db: Session, evacuee: schemas.EvacueeCreate):
    db_evacuee = models.Evacuee(**evacuee.dict())
    db.add(db_evacuee)
    db.commit()
    db.refresh(db_evacuee)
    return db_evacuee

def update_evacuee(db: Session, evacuee_id: str, evacuee_update: schemas.EvacueeUpdate):
    db_evacuee = db.query(models.Evacuee).filter(models.Evacuee.evacuee_id == evacuee_id).first()
    if db_evacuee:
        for key, value in evacuee_update.dict(exclude_unset=True).items():
            setattr(db_evacuee, key, value)
        db.commit()
        db.refresh(db_evacuee)
    return db_evacuee

def delete_evacuee(db: Session, evacuee_id: str):
    db_evacuee = db.query(models.Evacuee).filter(models.Evacuee.evacuee_id == evacuee_id).first()
    if db_evacuee:
        db.delete(db_evacuee)
        db.commit()
    return db_evacuee
