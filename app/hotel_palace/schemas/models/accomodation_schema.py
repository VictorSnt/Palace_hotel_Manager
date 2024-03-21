import datetime
from ninja import Schema

from datetime import date, time, datetime
from uuid import UUID

from ...schemas.models.customer_schema import CustomerOutSchema
from ...schemas.models.room_schemas import RoomOutSchema


class BaseAccommodationSchema(Schema):
    room: RoomOutSchema
    customer: CustomerOutSchema
    guest_quant: int
    checkin_date: date = datetime.now().date()
    
    
    
class AccommodationOutSchema(BaseAccommodationSchema):
    id: UUID
    is_active: bool
    checkout_date: date
    checkin_time: time
    checkout_time: time
    days_quant: int
    hosting_price: float
    total_hosting_price: float
    total_bill: float
    
class AccommodationInSchema(BaseAccommodationSchema):
    room: str
    customer: str
           