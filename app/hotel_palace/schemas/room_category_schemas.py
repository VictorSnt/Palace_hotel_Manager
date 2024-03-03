from typing import List
from ninja import ModelSchema
from ..models import RoomCategory


class RoomCategoryResponseSchema(ModelSchema):
    class Config:
        model = RoomCategory
        model_fields = [
            'id', 'description', 'one_guest_price',
            'two_guest_price', 'three_guest_price',
            'four_guest_price'
        ]

