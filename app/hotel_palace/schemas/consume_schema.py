from ninja import ModelSchema
from ..models import Consume


class ConsumeSchema(ModelSchema):
    class Config:
        model = Consume
        model_fields = [
            'id', 'room_reservation', 'room',
            'product', 'quantity', 'unit_price',
            'total'
        ]
        
