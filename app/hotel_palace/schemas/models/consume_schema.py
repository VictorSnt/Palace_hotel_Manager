import json
from django.shortcuts import get_object_or_404
from ninja_schema import ModelSchema, model_validator
from ...models import Accommodation, Consume, Product
from ...services.controller_services.consume_service import ConsumeService
from ...services.errors.exceptions import ValidationError

  
class ConsumeOutSchema(ModelSchema):
    class Config:
        model = Consume
        include = [
            'id', 'accommodation', 
            'product', 'quantity', 
            'unit_price', 'total' 
        ]
    
class CreateConsumeSchema(ModelSchema):
    class Config:
        model = Consume
        include = [
            'accommodation', 'product',
            'quantity'
        ]

    @model_validator('quantity')
    def validate_checkin_date(cls, quantity):
        if quantity <= 0:
            msg = json.dumps(
                {
                    'detail': 'A quantidade deve ser maior que 0'
                }
            )
            raise ValidationError(msg, 422)
        return quantity
    
    def model_dump(self, *args, **kwargs):
        schema_dict: dict = super().model_dump(*args, **kwargs)
        accommodation_id = schema_dict.get('accommodation')
        product_id = schema_dict.get('product')
        if accommodation_id and product_id:
            accom_instance = get_object_or_404(Accommodation, pk=accommodation_id)
            product_instance = get_object_or_404(Product, pk=product_id)
            schema_dict['accommodation'] = accom_instance
            schema_dict['product'] = product_instance
            schema_dict['unit_price'] = schema_dict['product'].price
            total = schema_dict['product'].price * schema_dict['quantity']
            schema_dict['total'] = total
            ConsumeService._parse_accommodation_info(schema_dict)
        return schema_dict
    