from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from api.database import Base

class Evacuee(Base):
    __tablename__ = "evacuee_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(String)
    address = Column(String)

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
