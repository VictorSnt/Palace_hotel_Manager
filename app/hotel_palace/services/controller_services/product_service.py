from typing import List

from ...database.handlers.database_handler import DataBaseHandler
from ...models import Product
from ...schemas.models.product_schema import (
    ProductInSchema, ProductOutSchema
)
from ...schemas.reponses.success_schemas import SuccessDetailed
from ...schemas.query_strings.database_filter import DBFilter
from ...services.base_service import BaseService


class ProductService(BaseService):
    
    PorductList = List[ProductOutSchema]
    Success201  = tuple[int, SuccessDetailed]


    @staticmethod
    def create(product: ProductInSchema) -> Success201:
        args = Product, product.model_dump()
        response = DataBaseHandler.try_to_create(*args)
        ProductService._validate_obj_creation(response)
        return 201, {'message': 'Criado com sucesso'}
    