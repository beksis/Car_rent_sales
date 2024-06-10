# app/main.py
from fastapi import FastAPI, HTTPException
from . import crud
from .database import init_db

app = FastAPI()

init_db()


@app.post("/categories/")
def create_category(name: str, description: str):
    return crud.create_category(name=name, description=description)


@app.get("/categories/{category_id}")
def read_category(category_id: int):
    category = crud.get_category(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@app.put("/categories/{category_id}")
def update_category(category_id: int, name: str, description: str):
    category = crud.update_category(category_id, name=name, description=description)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@app.delete("/categories/{category_id}")
def delete_category(category_id: int):
    success = crud.delete_category(category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"detail": "Category deleted"}


@app.post("/cars/")
def create_car(category_id: int, name: str, model: str, year: int, price: int):
    return crud.create_car(category_id=category_id, name=name, model=model, year=year, price=price)


@app.get("/cars/{car_id}")
def read_car(car_id: int):
    car = crud.get_car(car_id)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car


@app.put("/cars/{car_id}")
def update_car(car_id: int, category_id: int, name: str, model: str, year: int, price: int):
    car = crud.update_car(car_id, category_id=category_id, name=name, model=model, year=year, price=price)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car


@app.delete("/cars/{car_id}")
def delete_car(car_id: int):
    success = crud.delete_car(car_id)
    if not success:
        raise HTTPException(status_code=404, detail="Car not found")
    return {"detail": "Car deleted"}


@app.post("/rent_cars/")
def create_rent_car(car_id: int, renter_name: str, rent_date: str):
    return crud.create_rent_car(car_id=car_id, renter_name=renter_name, rent_date=rent_date)


@app.get("/rent_cars/{rent_car_id}")
def read_rent_car(rent_car_id: int):
    rent_car = crud.get_rent_car(rent_car_id)
    if not rent_car:
        raise HTTPException(status_code=404, detail="RentCar not found")
    return rent_car


@app.put("/rent_cars/{rent_car_id}")
def update_rent_car(rent_car_id: int, car_id: int, renter_name: str, rent_date: str):
    rent_car = crud.update_rent_car(rent_car_id, car_id=car_id, renter_name=renter_name, rent_date=rent_date)
    if not rent_car:
        raise HTTPException(status_code=404, detail="RentCar not found")
    return rent_car


@app.delete("/rent_cars/{rent_car_id}")
def delete_rent_car(rent_car_id: int):
    success = crud.delete_rent_car(rent_car_id)
    if not success:
        raise HTTPException(status_code=404, detail="RentCar not found")
    return {"detail": "RentCar deleted"}


@app.post("/sell_cars/")
def create_sell_car(car_id: int, buyer_name: str, sell_date: str):
    return crud.create_sell_car(car_id=car_id, buyer_name=buyer_name, sell_date=sell_date)


@app.get("/sell_cars/{sell_car_id}")
def read_sell_car(sell_car_id: int):
    sell_car = crud.get_sell_car(sell_car_id)
    if not sell_car:
        raise HTTPException(status_code=404, detail="SellCar not found")
    return sell_car


@app.put("/sell_cars/{sell_car_id}")
def update_sell_car(sell_car_id: int, car_id: int, buyer_name: str, sell_date: str):
    sell_car = crud.update_sell_car(sell_car_id, car_id=car_id, buyer_name=buyer_name, sell_date=sell_date)
    if not sell_car:
        raise HTTPException(status_code=404, detail="SellCar not found")
    return sell_car


@app.delete("/sell_cars/{sell_car_id}")
def delete_sell_car(sell_car_id: int):
    success = crud.delete_sell_car(sell_car_id)
    if not success:
        raise HTTPException(status_code=404, detail="SellCar not found")
    return {"detail": "SellCar deleted"}
