from ninja import ModelSchema
from ..models import Room


class RoomResponseSchema(ModelSchema):
    class Config:
        model = Room
        model_fields = ['id', 'number', 'status']
