from sqlalchemy.orm import Session
from city_temperature import models, schemas


def create_temperature(db: Session, temperature: schemas.temperature.TemperatureCreate):
    db_temp = models.temperature.Temperature(
        city_id=temperature.city_id,
        temperature=temperature.temperature
    )
    db.add(db_temp)
    db.commit()
    db.refresh(db_temp)
    return db_temp


def get_all_temperatures(db: Session):
    return db.query(models.temperature.Temperature).all()


def get_temperatures_by_city(db: Session, city_id: int):
    return db.query(models.temperature.Temperature).filter(
        models.temperature.Temperature.city_id == city_id
    ).all()
