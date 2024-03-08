from ninja import ModelSchema
from ...models import Product


class ProductsSchema(ModelSchema):
    class Config:
        model = Product
        model_fields = ['id', 'description', 'price']
