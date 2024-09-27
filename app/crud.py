from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime, timedelta

def get_orders_by_date(db: Session, date: datetime):
    return db.query(models.Order).filter(
        models.Order.walk_start >= date,
        models.Order.walk_start < date + timedelta(days=1)
    ).all()

def is_time_conflicted(db: Session, walk_start: datetime):
    conflicting_orders = db.query(models.Order).filter(
        models.Order.walk_start == walk_start
    ).all()
    return len(conflicting_orders) >= 2

def create_order(db: Session, order: schemas.OrderCreate, walk_end: datetime):
    db_order = models.Order(
        apartment_number=order.apartment_number,
        pet_name=order.pet_name,
        pet_breed=order.pet_breed,
        walk_start=order.walk_start,
        walk_end=walk_end
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
