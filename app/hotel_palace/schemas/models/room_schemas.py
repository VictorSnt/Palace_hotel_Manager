from ninja import ModelSchema
from ...models import Room


class RoomSchema(ModelSchema):
    class Config:
        model = Room
        model_fields = ['id', 'number', 'status']
