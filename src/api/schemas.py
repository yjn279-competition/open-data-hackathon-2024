from pydantic import BaseModel
from datetime import datetime, date
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

"""
MaterialDetailの基本的なスキーマを定義します。quantity, allergy_code, expiration_dateは任意フィールドです。
"""
class MaterialDetailBase(BaseModel):
    name: str
    genre: str
    quantity: Optional[int] = 0
    allergy_code: Optional[str] = None
    expiration_date: Optional[date] = None

"""
新しい材料詳細を作成するためのスキーマ。material_idとbranch_numberが必須フィールドです。
"""
class MaterialDetailCreate(MaterialDetailBase):
    material_id: str
    branch_number: str

"""
既存の材料詳細を更新するためのスキーマ。更新対象のフィールドのみを含めます。
"""
class MaterialDetailUpdate(MaterialDetailBase):
    pass

"""
データベースから取得した材料詳細を表現するためのスキーマ。タイムスタンプを含みます。
"""
class MaterialDetail(MaterialDetailBase):
    material_id: str
    branch_number: str
    update_at: datetime
    create_at: datetime

    class Config:
        orm_mode = True

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
