# app/crud.py
from sqlalchemy import create_engine, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select, update, delete
from .models import Category, Car, RentCar, SellCar

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

def row_to_dict(row, model: Table):
    if row is None:
        return None
    return {column.name: getattr(row, column.name) for column in model.__table__.columns}

def create_category(name: str, description: str):
    with engine.connect() as connection:
        result = connection.execute(
            Category.__table__.insert().values(name=name, description=description)
        )
        category_id = result.inserted_primary_key[0]
        return row_to_dict(connection.execute(select(Category).where(Category.id == category_id)).first(), Category)

def get_category(category_id: int):
    with engine.connect() as connection:
        result = connection.execute(select(Category).where(Category.id == category_id)).first()
        return row_to_dict(result, Category)

def update_category(category_id: int, name: str, description: str):
    with engine.connect() as connection:
        result = connection.execute(
            update(Category).where(Category.id == category_id).values(name=name, description=description)
        )
        if result.rowcount:
            return row_to_dict(connection.execute(select(Category).where(Category.id == category_id)).first(), Category)
        return None

def delete_category(category_id: int):
    with engine.connect() as connection:
        result = connection.execute(delete(Category).where(Category.id == category_id))
        return result.rowcount > 0

# Similar updates should be made to Car, RentCar, and SellCar functions

def create_car(category_id: int, name: str, model: str, year: int, price: int):
    with engine.connect() as connection:
        result = connection.execute(
            Car.__table__.insert().values(category_id=category_id, name=name, model=model, year=year, price=price)
        )
        car_id = result.inserted_primary_key[0]
        return row_to_dict(connection.execute(select(Car).where(Car.id == car_id)).first(), Car)

def get_car(car_id: int):
    with engine.connect() as connection:
        result = connection.execute(select(Car).where(Car.id == car_id)).first()
        return row_to_dict(result, Car)

def update_car(car_id: int, category_id: int, name: str, model: str, year: int, price: int):
    with engine.connect() as connection:
        result = connection.execute(
            update(Car).where(Car.id == car_id).values(category_id=category_id, name=name, model=model, year=year, price=price)
        )
        if result.rowcount:
            return row_to_dict(connection.execute(select(Car).where(Car.id == car_id)).first(), Car)
        return None

def delete_car(car_id: int):
    with engine.connect() as connection:
        result = connection.execute(delete(Car).where(Car.id == car_id))
        return result.rowcount > 0

def create_rent_car(car_id: int, renter_name: str, rent_date: str):
    with engine.connect() as connection:
        result = connection.execute(
            RentCar.__table__.insert().values(car_id=car_id, renter_name=renter_name, rent_date=rent_date)
        )
        rent_car_id = result.inserted_primary_key[0]
        return row_to_dict(connection.execute(select(RentCar).where(RentCar.id == rent_car_id)).first(), RentCar)

def get_rent_car(rent_car_id: int):
    with engine.connect() as connection:
        result = connection.execute(select(RentCar).where(RentCar.id == rent_car_id)).first()
        return row_to_dict(result, RentCar)

def update_rent_car(rent_car_id: int, car_id: int, renter_name: str, rent_date: str):
    with engine.connect() as connection:
        result = connection.execute(
            update(RentCar).where(RentCar.id == rent_car_id).values(car_id=car_id, renter_name=renter_name, rent_date=rent_date)
        )
        if result.rowcount:
            return row_to_dict(connection.execute(select(RentCar).where(RentCar.id == rent_car_id)).first(), RentCar)
        return None

def delete_rent_car(rent_car_id: int):
    with engine.connect() as connection:
        result = connection.execute(delete(RentCar).where(RentCar.id == rent_car_id))
        return result.rowcount > 0

def create_sell_car(car_id: int, buyer_name: str, sell_date: str):
    with engine.connect() as connection:
        result = connection.execute(
            SellCar.__table__.insert().values(car_id=car_id, buyer_name=buyer_name, sell_date=sell_date)
        )
        sell_car_id = result.inserted_primary_key[0]
        return row_to_dict(connection.execute(select(SellCar).where(SellCar.id == sell_car_id)).first(), SellCar)

def get_sell_car(sell_car_id: int):
    with engine.connect() as connection:
        result = connection.execute(select(SellCar).where(SellCar.id == sell_car_id)).first()
        return row_to_dict(result, SellCar)

def update_sell_car(sell_car_id: int, car_id: int, buyer_name: str, sell_date: str):
    with engine.connect() as connection:
        result = connection.execute(
            update(SellCar).where(SellCar.id == sell_car_id).values(car_id=car_id, buyer_name=buyer_name, sell_date=sell_date)
        )
        if result.rowcount:
            return row_to_dict(connection.execute(select(SellCar).where(SellCar.id == sell_car_id)).first(), SellCar)
        return None

def delete_sell_car(sell_car_id: int):
    with engine.connect() as connection:
        result = connection.execute(delete(SellCar).where(SellCar.id == sell_car_id))
        return result.rowcount > 0
