from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app import crud, schemas, database

app = FastAPI()


@app.get("/orders/{date}", response_model=list[schemas.OrderResponse])
def read_orders(date: str, db: Session = Depends(database.get_db)):
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format, should be YYYY-MM-DD")

    return crud.get_orders_by_date(db, date)


@app.post("/orders/", response_model=schemas.OrderResponse)
def create_order(order: schemas.OrderCreate, db: Session = Depends(database.get_db)):
    # Validate walk_start
    if order.walk_start.hour < 7 or order.walk_start.hour > 23 or (order.walk_start.minute not in [0, 30]):
        raise HTTPException(status_code=400, detail="Invalid start time, should be 07:00, 07:30, ..., 23:00 or 23:30")

    walk_end = order.walk_start + timedelta(minutes=30)
    if walk_end.hour > 23:
        raise HTTPException(status_code=400, detail="Walk end time exceeds 23:30")

    if crud.is_time_conflicted(db, order.walk_start):
        raise HTTPException(status_code=400, detail="Two walks are already scheduled for this time")

    return crud.create_order(db, order, walk_end)
