from uuid import UUID
from ninja import ModelSchema
from ...models import Room
from ...utils.enums.room_status import RoomStatus

class BaseRoomSchema(ModelSchema):
    class Config:
        model = Room
        model_fields = ['number', 'status', 'category']

class RoomSchema(BaseRoomSchema):
    id: UUID

class RoomCreationSchema(BaseRoomSchema):
    pass
