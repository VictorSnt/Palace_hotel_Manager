import json
from django.shortcuts import get_object_or_404
from ninja_schema import ModelSchema, model_validator
from ...models import Category, Room
from ...services.errors.exceptions import ValidationError


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
        category_id = schema_dict.get('category', False)
        if category_id:
            instance = get_object_or_404(Category, pk=category_id)
            schema_dict['category'] = instance
        return schema_dict

    @model_validator('number')
    def validate_number(cls, number: str):
        if not number.isnumeric():
            msg = json.dumps(
                {
                    'field': 'number',
                    'detail': 'deve ser um string numerico de ate 3 digitos'
                }
            )
            raise ValidationError(msg, 422)
        return number
    
    @model_validator('status')
    def validate_enum(cls, status):
        return status.value if status else None
    
class RoomUpdaterSchema(CreateRoomSchema):
    class Config:
        model = Room
        include = ['number', 'status', 'category']
        optional = ['number', 'status', 'category']
   