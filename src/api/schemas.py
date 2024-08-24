from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class EvacueeBase(BaseModel):
    name: str
    age: int
    gender: str
    address: str

class EvacueeCreate(EvacueeBase):
    pass

class Evacuee(EvacueeBase):
    id: int

    class Config:
        orm_mode: True

class MaterialDetailBase(BaseModel):
    description: str
    created_at: datetime

class MaterialDetailCreate(MaterialDetailBase):
    pass

class MaterialDetail(MaterialDetailBase):
    id: int
    material_id: int

    class Config:
        orm_mode: True

class MaterialBase(BaseModel):
    name: str
    quantity: int

class MaterialCreate(MaterialBase):
    details: List[MaterialDetailCreate]

class Material(MaterialBase):
    id: int
    details: List[MaterialDetail]

    class Config:
        orm_mode: True

class ShelterBase(BaseModel):
    name: str
    location: str
    capacity: int
    current_occupancy: int

class ShelterCreate(ShelterBase):
    pass

class Shelter(ShelterBase):
    id: int

    class Config:
        orm_mode: True
