from uuid import UUID
from ninja import Schema
from ...schemas.models.accomodation_schema import AccommodationOutSchema
from ...schemas.models.product_schema import ProductOutSchema


class BaseConsumeSchema(Schema):
    accommodation: AccommodationOutSchema
    product: ProductOutSchema
    quantity: float
    
class ConsumeOutSchema(BaseConsumeSchema):
    id: UUID
    unit_price: float
    total: float
    
class ConsumeInSchema(BaseConsumeSchema):
    accommodation: str
    product: str
