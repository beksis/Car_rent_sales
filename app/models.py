# app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)

    cars = relationship("Car", back_populates="category")

class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    name = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer)
    price = Column(Integer)

    category = relationship("Category", back_populates="cars")
    rent_details = relationship("RentCar", uselist=False, back_populates="car")
    sell_details = relationship("SellCar", uselist=False, back_populates="car")

class RentCar(Base):
    __tablename__ = 'rent_cars'

    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey('cars.id'))
    renter_name = Column(String)
    rent_date = Column(String)

    car = relationship("Car", back_populates="rent_details")

class SellCar(Base):
    __tablename__ = 'sell_cars'

    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey('cars.id'))
    buyer_name = Column(String)
    sell_date = Column(String)

    car = relationship("Car", back_populates="sell_details")
