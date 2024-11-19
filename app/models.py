from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


animal_guider = Table('animal_guider', Base.metadata,
    Column('animal_id', Integer, ForeignKey('animals.id')),
    Column('guider_id', Integer, ForeignKey('guiders.id'))
)

guest_guider = Table('guest_guider', Base.metadata,
    Column('guest_id', Integer, ForeignKey('guests.id')),
    Column('guider_id', Integer, ForeignKey('guiders.id'))
)

class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    species = Column(String)
    age = Column(Integer)
    guiders = relationship("Guider", secondary=animal_guider, back_populates="animals")

class Guider(Base):
    __tablename__ = "guiders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    service_hours = Column(Integer)
    animals = relationship("Animal", secondary=animal_guider, back_populates="guiders")
    guests = relationship("Guest", secondary=guest_guider, back_populates="guiders")

class Guest(Base):
    __tablename__ = "guests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    visit_date = Column(String)
    guiders = relationship("Guider", secondary=guest_guider, back_populates="guests")