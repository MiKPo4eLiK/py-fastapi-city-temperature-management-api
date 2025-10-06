from sqlalchemy.orm import Session
from city_temperature.models.city import City
from city_temperature import schemas


def create_city(db: Session, city: schemas.city.CityCreate):
    db_city = City(
        name=city.name,
        additional_info=city.additional_info
    )
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city


def get_cities(db: Session, skip: int = 0, limit: int = 10):
    return db.query(City).offset(skip).limit(limit).all()


def get_city(db: Session, city_id: int):
    return db.query(City).filter(City.id == city_id).first()


def update_city(db: Session, city_id: int, city_update: schemas.city.CityCreate):
    db_city = get_city(db, city_id)
    if not db_city:
        return None
    db_city.name = city_update.name
    db_city.additional_info = city_update.additional_info
    db.commit()
    db.refresh(db_city)
    return db_city


def delete_city(db: Session, city_id: int):
    db_city = get_city(db, city_id)
    if not db_city:
        return None
    db.delete(db_city)
    db.commit()
    return db_city

