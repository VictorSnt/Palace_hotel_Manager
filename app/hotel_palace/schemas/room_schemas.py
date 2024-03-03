from typing import List
from uuid import UUID
from ninja import ModelSchema, Schema
from ..models import Room


class RoomResponseSchema(ModelSchema):
    class Config:
        model = Room
        model_fields = ['id', 'number', 'status']

class GetRoomsQuery(Schema):
    ids: List[UUID]