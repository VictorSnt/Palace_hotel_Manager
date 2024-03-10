from ninja import ModelSchema
from ...models import Consume


class ConsumeSchema(ModelSchema):
    class Config:
        model = Consume
        model_fields = [
            'id', 'accommodation', 'room',
            'product', 'quantity', 'unit_price',
            'total'
        ]
        
