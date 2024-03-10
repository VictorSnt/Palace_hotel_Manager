from uuid import UUID
from ninja import Schema
from ...models import Category


class BaseCategorySchema(Schema):
    description: str
    one_guest_price: float
    two_guest_price: float
    three_guest_price: float
    four_guest_price: float

class CategoryOutSchema(BaseCategorySchema):
    id: UUID

class CategoryInSchema(BaseCategorySchema):
    pass
