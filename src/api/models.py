from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, ARRAY, TIMESTAMP, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from api.database import Base

class Evacuee(Base):
    """
    Evacueeテーブルを表すSQLAlchemyモデル。
    避難者情報を管理します。
    """
    __tablename__ = "evacuee_table"

    evacuee_id = Column(String(64), primary_key=True, index=True)  # 避難者ID（主キー）
    is_safety = Column(Boolean)  # 安否確認
    shelter_code = Column(String(64), ForeignKey('shelter_table.shelter_code'))  # 避難所コード（外部キー）
    allergy_code = Column(String(2))  # アレルギーコード
    update_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())  # レコード更新時のタイムスタンプ
    create_at = Column(TIMESTAMP, server_default=func.now())  # レコード作成時のタイムスタンプ

    # 避難所とのリレーションシップ
    shelter = relationship("Shelter", back_populates="evacuees")

class MyNumberCard(Base):
    __tablename__ = "my_number_card"
    card_number = Column(String, primary_key=True, index=True)
    full_name = Column(String)
    birth_date = Column(Date)
    address = Column(String)


class Material(Base):
    """
    Materialテーブルを表すSQLAlchemyモデル。
    材料情報を管理します。
    """
    __tablename__ = "materials_table"

    material_id = Column(String(64), primary_key=True, index=True)  # 材料ID（主キー）
    name = Column(String(256), nullable=False)  # 材料名
    allergy_code = Column(String(2))  # アレルギーコード
    genre = Column(String(64), nullable=False)  # ジャンル
    update_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())  # レコード更新時のタイムスタンプ
    create_at = Column(TIMESTAMP, server_default=func.now())  # レコード作成時のタイムスタンプ

    # MaterialDetailとのリレーションシップ
    details = relationship("MaterialDetail", back_populates="material")

class MaterialDetail(Base):
    """
    MaterialDetailテーブルを表すSQLAlchemyモデル。
    材料の詳細情報を管理します。
    """
    __tablename__ = "materials_detail_table"

    material_id = Column(String(64), ForeignKey('materials_table.material_id'), primary_key=True)  # 材料ID（外部キー、主キー）
    branch_number = Column(String(16), primary_key=True)  # ブランチ番号（主キー）
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
    """
    Shelterテーブルを表すSQLAlchemyモデル。
    避難所情報を管理します。
    """
    __tablename__ = "shelter_table"

    shelter_code = Column(String(64), primary_key=True, index=True)  # 避難所コード（主キー）
    name = Column(String(256), nullable=False)  # 避難所の名前
    strong_point = Column(ARRAY(String))  # 特徴
    postal_code = Column(String(8))  # 郵便番号
    prefectures = Column(String(32), nullable=False)  # 都道府県
    address = Column(String(256), nullable=False)  # 住所
    total_count = Column(Integer, default=0)  # 現在の避難者数
    capacity = Column(Integer, default=0)  # 収容人数
    availability_status = Column(String(1), server_default="2")  # 空き状況
    update_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())  # レコード更新時のタイムスタンプ
    create_at = Column(TIMESTAMP, server_default=func.now())  # レコード作成時のタイムスタンプ

    # 避難者とのリレーションシップ
    evacuees = relationship("Evacuee", back_populates="shelter")

    # availability_statusの値を制約
    __table_args__ = (
        CheckConstraint('availability_status IN (\'0\', \'1\', \'2\')', name='check_availability_status'),
    )

class DeviceData(Base):
    """
    BLEデバイス情報を管理するためのモデル。
    """
    __tablename__ = "ble_device_data"

    id = Column(Integer, primary_key=True, index=True)  # 主キーID
    device_id = Column(String(64), nullable=False, index=True)  # BLEデバイスのID
    data = Column(String(256), nullable=False)  # デバイスから取得したデータ（例: バッテリーレベル）
    create_at = Column(TIMESTAMP, server_default=func.now())  # レコード作成時のタイムスタンプ
    update_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())  # レコード更新時のタイムスタンプ