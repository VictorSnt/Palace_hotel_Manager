from uuid import UUID
from ninja import Schema

from ...schemas.models.category_schemas import(
    CategoryResponseSchema
)


class BaseRoomSchema(Schema):
    number: str
    status: str

class RoomOutSchema(BaseRoomSchema):
    id: UUID
    category: CategoryResponseSchema

class RoomInSchema(BaseRoomSchema):
    category: str
