from pydantic import BaseModel
from datetime import datetime

class OrderCreate(BaseModel):
    apartment_number: str
    pet_name: str
    pet_breed: str
    walk_start: datetime

class OrderResponse(OrderCreate):
    id: int
    walk_end: datetime
