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

"""
Materialの基本的なスキーマを定義します。allergy_codeは任意フィールドです。
"""
class MaterialBase(BaseModel):
    name: str
    genre: str
    allergy_code: Optional[str] = None

"""
新しい材料を作成するためのスキーマ。material_idが必須フィールドです。
"""
class MaterialCreate(MaterialBase):
    material_id: str

"""
既存の材料を更新するためのスキーマ。更新対象のフィールドのみを含めます。
"""
class MaterialUpdate(MaterialBase):
    pass

"""
データベースから取得した材料を表現するためのスキーマ。タイムスタンプを含みます。
"""
class Material(MaterialBase):
    material_id: str
    update_at: datetime
    create_at: datetime

    class Config:
        orm_mode = True

"""
Shelterの基本的なスキーマを定義します。strong_point, postal_code, total_count, capacity, availability_statusは任意フィールドです。
"""
class ShelterBase(BaseModel):
    name: str
    prefectures: str
    address: str
    strong_point: Optional[List[str]] = None
    postal_code: Optional[str] = None
    total_count: Optional[int] = 0
    capacity: Optional[int] = 0
    availability_status: Optional[str] = "2"

"""
新しい避難所を作成するためのスキーマ。shelter_codeが必須フィールドです。
"""
class ShelterCreate(ShelterBase):
    shelter_code: str

"""
既存の避難所を更新するためのスキーマ。更新対象のフィールドのみを含めます。
"""
class ShelterUpdate(ShelterBase):
    pass

"""
データベースから取得した避難所を表現するためのスキーマ。タイムスタンプを含みます。
"""
class Shelter(ShelterBase):
    shelter_code: str
    update_at: datetime
    create_at: datetime

    class Config:
        orm_mode = True
