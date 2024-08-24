from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, TIMESTAMP
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

class Material(Base):
    __tablename__ = "materials_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer)

    details = relationship("MaterialDetail", back_populates="material")

class MaterialDetail(Base):
    __tablename__ = "materials_detail_table"

    id = Column(Integer, primary_key=True, index=True)
    material_id = Column(Integer, ForeignKey("materials_table.id"))
    description = Column(String)
    created_at = Column(TIMESTAMP)

    material = relationship("Material", back_populates="details")

class Shelter(Base):
    __tablename__ = "shelter_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    capacity = Column(Integer)
    current_occupancy = Column(Integer)
