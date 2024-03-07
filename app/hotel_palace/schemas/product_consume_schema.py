from ninja import ModelSchema
from ..models import ProductConsume


class ProductConsumeSchema(ModelSchema):
    class Config:
        model = ProductConsume
        model_fields = [
            'id', 'room_reservation', 'room',
            'product', 'quantity', 'unit_price',
            'total'
        ]
        
