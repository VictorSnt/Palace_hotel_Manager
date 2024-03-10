from uuid import UUID
from ninja import Schema


class BaseProductSchema(Schema):
    description: str
    price: float

class ProductOutSchema(BaseProductSchema):
    id: UUID

class ProductInSchema(BaseProductSchema):
    pass
