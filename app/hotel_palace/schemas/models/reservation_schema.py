from uuid import UUID
from ninja import Schema
from ...schemas.models.room_schemas import(
    RoomOutSchema
)


class BaseReservationSchema(Schema):
    customer_name: str
    room: RoomOutSchema
    checkin_date: str

class ReservationOutSchema(BaseReservationSchema):
    id: UUID

class ReservationInSchema(BaseReservationSchema):
    room: str
