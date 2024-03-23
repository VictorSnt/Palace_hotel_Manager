from django.shortcuts import get_object_or_404
from ninja_schema import ModelSchema, model_validator
from ...models import Category, Room
from ninja import Schema


class RoomOutSchema(ModelSchema):
    class Config:
        model = Room
        include = [
            'id', 'number', 
            'status', 'category'
        ]


class CreateRoomSchema(ModelSchema):
    class Config:
        model = Room
        include = ['number', 'status', 'category']
    
    def model_dump(self, *args, **kwargs):
        schema_dict = super().model_dump(*args, **kwargs)
        category_id = schema_dict.get('category')
        instance = get_object_or_404(Category, pk=category_id)
        schema_dict['category'] = instance
        return schema_dict

    @model_validator('status')
    def validate_enum(cls, enum):
        return enum.value if enum else None
    
class RoomUpdaterSchema(Schema):
    number: str = None
    status: str = None
    category: str = None