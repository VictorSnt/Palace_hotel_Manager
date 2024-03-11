from uuid import UUID
from ninja import Schema
from ...schemas.models.accomodation_schema import AccommodationOutSchema
from ...schemas.models.product_schema import ProductOutSchema
from ...schemas.models.room_schemas import RoomOutSchema


class BaseConsumeSchema(Schema):
    accommodation: AccommodationOutSchema
    room: RoomOutSchema
    product: ProductOutSchema
    quantity: float
    unit_price: float
    total: float
    
class ConsumeOutSchema(BaseConsumeSchema):
    id: UUID

class ConsumeInSchema(BaseConsumeSchema):
    room: str
    accommodation: str
    product: str
