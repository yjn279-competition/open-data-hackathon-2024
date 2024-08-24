from sqlalchemy.orm import Session
from api import models, schemas

def get_shelters(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Shelter).offset(skip).limit(limit).all()

def get_shelter(db: Session, shelter_id: int):
    return db.query(models.Shelter).filter(models.Shelter.id == shelter_id).first()

def create_shelter(db: Session, shelter: schemas.ShelterCreate):
    db_shelter = models.Shelter(**shelter.dict())
    db.add(db_shelter)
    db.commit()
    db.refresh(db_shelter)
    return db_shelter
