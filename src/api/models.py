from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from api.database import Base

class Evacuee(Base):
    __tablename__ = "evacuee_table"

    evacuee_id = Column(String(64), primary_key=True, index=True)
    is_safety = Column(Boolean)
    shelter_code = Column(String(64))
    allergy_code = Column(String(2))
    update_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    create_at = Column(TIMESTAMP, server_default=func.now())

"""
Materialテーブルを表すSQLAlchemyモデル。
"""
class Material(Base):
    __tablename__ = "materials_table"

    material_id = Column(String(64), primary_key=True, index=True)  # 主キー
    name = Column(String(256), nullable=False)  # 材料の名前
    allergy_code = Column(String(2))  # アレルギーコード
    genre = Column(String(64), nullable=False)  # ジャンル
    update_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())  # レコード更新時のタイムスタンプ
    create_at = Column(TIMESTAMP, server_default=func.now())  # レコード作成時のタイムスタンプ

    # MaterialDetailとのリレーションシップ
    details = relationship("MaterialDetail", back_populates="material")

"""
MaterialDetailテーブルを表すSQLAlchemyモデル。
"""
class MaterialDetail(Base):
    __tablename__ = "materials_detail_table"

    material_id = Column(String(64), ForeignKey('materials_table.material_id'), primary_key=True)  # 外部キー
    branch_number = Column(String(16), primary_key=True)  # ブランチ番号
    name = Column(String(256), nullable=False)  # 材料の名前
    quantity = Column(Integer, default=0)  # 数量
    allergy_code = Column(String(2))  # アレルギーコード
    genre = Column(String(64), nullable=False)  # ジャンル
    update_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())  # レコード更新時のタイムスタンプ
    create_at = Column(TIMESTAMP, server_default=func.now())  # レコード作成時のタイムスタンプ
    expiration_date = Column(Date)  # 有効期限

    # Materialとのリレーションシップ
    material = relationship("Material", back_populates="details")


class Shelter(Base):
    __tablename__ = "shelter_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    capacity = Column(Integer)
    current_occupancy = Column(Integer)
