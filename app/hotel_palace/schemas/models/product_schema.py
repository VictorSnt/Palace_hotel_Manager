from ninja_schema import ModelSchema
from ...models import Product


class ProductOutSchema(ModelSchema):
    class Config:
        model = Product
        include = ['id', 'description', 'price']

class CreateProductSchema(ModelSchema):
    class Config:
        model = Product
        include = ['description', 'price']
        
class UpdateProductSchema(ModelSchema):
    class Config:
        model = Product
        include = ['description', 'price']
        optional = ['description', 'price']
    