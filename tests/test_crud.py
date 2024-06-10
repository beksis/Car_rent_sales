# tests/test_crud.py
import pytest
from app import crud
from app.database import init_db, engine
from app.models import Base

@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown_db():
    # Инициализация базы данных перед каждым тестом
    init_db()
    yield
    # Очистка базы данных после каждого теста
    Base.metadata.drop_all(bind=engine)

def test_create_category():
    category = crud.create_category(name="SUV", description="Sport Utility Vehicle")
    assert category['name'] == "SUV"
    assert category['description'] == "Sport Utility Vehicle"

def test_read_category():
    category = crud.create_category(name="SUV", description="Sport Utility Vehicle")
    fetched_category = crud.get_category(category_id=category['id'])
    assert fetched_category['name'] == "SUV"
    assert fetched_category['description'] == "Sport Utility Vehicle"

def test_update_category():
    category = crud.create_category(name="SUV", description="Sport Utility Vehicle")
    updated_category = crud.update_category(category_id=category['id'], name="Crossover", description="Small SUV")
    assert updated_category['name'] == "Crossover"
    assert updated_category['description'] == "Small SUV"

def test_delete_category():
    category = crud.create_category(name="SUV", description="Sport Utility Vehicle")
    success = crud.delete_category(category_id=category['id'])
    assert success
    assert crud.get_category(category_id=category['id']) is None

# Similar tests can be added for Car, RentCar, and SellCar
