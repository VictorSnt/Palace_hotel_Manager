from ...services.errors.exceptions import ValidationError
from ninja_schema import ModelSchema, model_validator
from ...models import Product
import json


class ProductOutSchema(ModelSchema):
    class Config:
        model = Product
        include = ['id', 'description', 'price']

class CreateProductSchema(ModelSchema):
    class Config:
        model = Product
        include = ['description', 'price']
    
    @model_validator('description')
    def validate_description(cls, description):
        if len(description) < 3:
            msg = json.dumps({'detail': 'A descrição precisa de 3 letras ou +'})
            raise ValidationError(msg, 422)
        return description
    
    @model_validator('price')
    def validate_price(cls, price):
        if price <= 0:
            msg = json.dumps({'detail': 'O preço deve ser maior que 0'})
            raise ValidationError(msg, 422)
        return price
    
class UpdateProductSchema(CreateProductSchema):
    class Config:
        model = Product
        include = ['description', 'price']
        optional = ['description', 'price']
    