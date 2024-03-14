from typing import List

from ...database.handlers.database_handler import DataBaseHandler
from ...models import Product
from ...schemas.models.product_schema import (
    ProductInSchema, ProductOutSchema
)
from ...schemas.reponses.success_schemas import SuccessDetailed
from ...schemas.query_strings.database_filter import DBFilter
from ...validators.id_validator import IDValidator
from ...validators.db_validators import DBValidator
from ...services.trasformators.parsers import IDParser

class ProductService:
    
    PorductList = List[ProductOutSchema]
    Success201  = tuple[int, SuccessDetailed]

    @staticmethod
    def get_all(dbfilter: DBFilter) -> PorductList:
        DBValidator.is_valid_db_field(Product, dbfilter.order_by)  
        products = DataBaseHandler.get_all(Product, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(products)
        return products
    
    @staticmethod
    def get_by_ids(ids: str, dbfilter: DBFilter) -> PorductList:
        DBValidator.is_valid_db_field(Product, dbfilter.order_by)  
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        products = DataBaseHandler.get_by_ids(Product, parsed_ids, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(products)
        return products

    @staticmethod
    def create(product: ProductInSchema) -> Success201:
        args = Product, product.model_dump()
        product_obj, is_created = DataBaseHandler.try_to_create(*args)
        DBValidator.is_created_or_already_exist(is_created, product_obj)
        return 201, {'message': 'Criado com sucesso'}
    