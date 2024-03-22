from uuid import UUID
from ninja import Schema

from ...schemas.models.category_schemas import(
    CategoryOutSchema
)


class BaseRoomSchema(Schema):
    number: str
    status: str

class RoomOutSchema(BaseRoomSchema):
    id: UUID
    category: CategoryOutSchema

class RoomInSchema(BaseRoomSchema):
    category: str

class RoomUpdaterSchema(Schema):
    number: str = None
    status: str = None
    category: str = None