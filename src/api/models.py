from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, ARRAY, TIMESTAMP, CheckConstraint
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

    material_id = Column(String(64), primary_key=True, index=True)
    name = Column(String(256), nullable=False)
    allergy_code = Column(String(2))
    genre = Column(String(64), nullable=False)
    update_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    create_at = Column(TIMESTAMP, server_default=func.now())

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


"""
Shelterテーブルを表すSQLAlchemyモデル。
"""
class Shelter(Base):
    __tablename__ = "shelter_table"

    shelter_code = Column(String(64), primary_key=True, index=True)  # 主キー
    name = Column(String(256), nullable=False)  # 避難所の名前
    strong_point = Column(ARRAY(String))  # 特徴
    postal_code = Column(String(8))  # 郵便番号
    prefectures = Column(String(32), nullable=False)  # 都道府県
    address = Column(String(256), nullable=False)  # 住所
    total_count = Column(Integer, default=0)  # 現在の人数
    capacity = Column(Integer, default=0)  # 収容人数
    availability_status = Column(String(1), server_default="2")  # 空き状況
    update_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())  # レコード更新時のタイムスタンプ
    create_at = Column(TIMESTAMP, server_default=func.now())  # レコード作成時のタイムスタンプ

    __table_args__ = (
        CheckConstraint('availability_status IN (\'0\', \'1\', \'2\')', name='check_availability_status'),
    )

