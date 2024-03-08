from typing import List
from ninja import ModelSchema
from ...models import Category


class CategoryResponseSchema(ModelSchema):
    class Config:
        model = Category
        model_fields = [
            'id', 'description', 'one_guest_price',
            'two_guest_price', 'three_guest_price',
            'four_guest_price'
        ]

