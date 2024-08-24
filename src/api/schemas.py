from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class EvacueeBase(BaseModel):
    is_safety: Optional[bool] = None
    shelter_code: Optional[str] = None
    allergy_code: Optional[str] = None

class EvacueeCreate(EvacueeBase):
    evacuee_id: str

class EvacueeUpdate(EvacueeBase):
    pass

class Evacuee(EvacueeBase):
    evacuee_id: str
    update_at: datetime
    create_at: datetime

    class Config:
        orm_mode = True

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
