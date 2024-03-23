from ninja_schema import ModelSchema
from ...models import Category


class CreateCategorySchema(ModelSchema):
    class Config:
        model = Category
        include = [
            'description', 'one_guest_price',
            'two_guest_price', 'three_guest_price',
            'four_guest_price' 
        ]
        
class CategoryOutSchema(ModelSchema):
    class Config:
        model = Category
        include = [
            'id', 'description', 
            'one_guest_price', 'two_guest_price',
            'three_guest_price', 'four_guest_price' 
        ]