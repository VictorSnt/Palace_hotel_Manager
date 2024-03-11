from ninja import Schema

from datetime import date, time
from uuid import UUID

from ...schemas.models.customer_schema import CustomerOutSchema
from ...schemas.models.room_schemas import RoomOutSchema


class BaseAccommodationSchema(Schema):
    room: RoomOutSchema
    customer: CustomerOutSchema
    guest_quant: int
    is_active: bool
    days_quant: int
    checkin_date: date
    checkout_date: date
    checkin_time: time
    checkout_time: time
    hosting_price: float
    total_hosting_price: float
    total_bill: float
    
class AccommodationOutSchema(BaseAccommodationSchema):
    id: UUID

class AccommodationInSchema(BaseAccommodationSchema):
    room: str
    customer: str
           