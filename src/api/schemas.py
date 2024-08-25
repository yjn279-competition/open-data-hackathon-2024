from pydantic import BaseModel
from datetime import datetime, date
from typing import List, Optional

class EvacueeBase(BaseModel):
    """
    避難者の基本的なスキーマを定義します。
    """
    is_safety: Optional[bool] = None  # 安否確認
    shelter_code: Optional[str] = None  # 避難所コード
    allergy_code: Optional[str] = None  # アレルギーコード

class EvacueeCreate(EvacueeBase):
    """
    新しい避難者を作成するためのスキーマ。
    evacuee_idが必須フィールドです。
    """
    evacuee_id: str  # 避難者ID

class EvacueeUpdate(EvacueeBase):
    """
    既存の避難者情報を更新するためのスキーマ。
    更新対象のフィールドのみを含めます。
    """
    pass

class Evacuee(EvacueeBase):
    """
    データベースから取得した避難者を表現するためのスキーマ。
    タイムスタンプを含みます。
    """
    evacuee_id: str  # 避難者ID
    update_at: datetime  # 更新日時
    create_at: datetime  # 作成日時

    class Config:
        orm_mode = True  # ORMモードを有効にして、ORMモデルとの互換性を持たせます。

class MaterialDetailBase(BaseModel):
    """
    MaterialDetailの基本的なスキーマを定義します。
    quantity, allergy_code, expiration_dateは任意フィールドです。
    """
    name: str  # 材料の名前
    genre: str  # ジャンル
    quantity: Optional[int] = 0  # 数量
    allergy_code: Optional[str] = None  # アレルギーコード
    expiration_date: Optional[date] = None  # 有効期限

class MaterialDetailCreate(MaterialDetailBase):
    """
    新しい材料詳細を作成するためのスキーマ。
    material_idとbranch_numberが必須フィールドです。
    """
    material_id: str  # 材料ID
    branch_number: str  # ブランチ番号

class MaterialDetailUpdate(MaterialDetailBase):
    """
    既存の材料詳細を更新するためのスキーマ。
    更新対象のフィールドのみを含めます。
    """
    pass

class MaterialDetail(MaterialDetailBase):
    """
    データベースから取得した材料詳細を表現するためのスキーマ。
    タイムスタンプを含みます。
    """
    material_id: str  # 材料ID
    branch_number: str  # ブランチ番号
    update_at: datetime  # 更新日時
    create_at: datetime  # 作成日時

    class Config:
        orm_mode = True  # ORMモードを有効にして、ORMモデルとの互換性を持たせます。

class MaterialBase(BaseModel):
    """
    Materialの基本的なスキーマを定義します。
    allergy_codeは任意フィールドです。
    """
    name: str  # 材料の名前
    genre: str  # ジャンル
    allergy_code: Optional[str] = None  # アレルギーコード

class MaterialCreate(MaterialBase):
    """
    新しい材料を作成するためのスキーマ。
    material_idが必須フィールドです。
    """
    material_id: str  # 材料ID

class MaterialUpdate(MaterialBase):
    """
    既存の材料を更新するためのスキーマ。
    更新対象のフィールドのみを含めます。
    """
    pass

class Material(MaterialBase):
    """
    データベースから取得した材料を表現するためのスキーマ。
    タイムスタンプを含みます。
    """
    material_id: str  # 材料ID
    update_at: datetime  # 更新日時
    create_at: datetime  # 作成日時

    class Config:
        orm_mode = True  # ORMモードを有効にして、ORMモデルとの互換性を持たせます。

class ShelterBase(BaseModel):
    """
    Shelterの基本的なスキーマを定義します。
    strong_point, postal_code, total_count, capacity, availability_statusは任意フィールドです。
    """
    name: str  # 避難所の名前
    prefectures: str  # 都道府県
    address: str  # 住所
    strong_point: Optional[List[str]] = None  # 特徴
    postal_code: Optional[str] = None  # 郵便番号
    total_count: Optional[int] = 0  # 現在の避難者数
    capacity: Optional[int] = 0  # 収容人数
    availability_status: Optional[str] = "2"  # 空き状況

class ShelterCreate(ShelterBase):
    """
    新しい避難所を作成するためのスキーマ。
    shelter_codeが必須フィールドです。
    """
    shelter_code: str  # 避難所コード

class ShelterUpdate(ShelterBase):
    """
    既存の避難所を更新するためのスキーマ。
    更新対象のフィールドのみを含めます。
    """
    pass

class Shelter(ShelterBase):
    """
    データベースから取得した避難所を表現するためのスキーマ。
    タイムスタンプを含みます。
    """
    shelter_code: str  # 避難所コード
    update_at: datetime  # 更新日時
    create_at: datetime  # 作成日時

    class Config:
        orm_mode = True  # ORMモードを有効にして、ORMモデルとの互換性を持たせます。
