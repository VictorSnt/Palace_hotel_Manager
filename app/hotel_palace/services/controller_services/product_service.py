from typing import List
from ...database.handlers.database_handler import DataBaseHandler
from ...models import Product
from ...schemas.models.product_schema import (
    ProductInSchema, ProductOutSchema
)
from ...schemas.query_strings.database_filter import DBFilter
from ...validators.id_validator import IDValidator
from ...validators.db_validators import DBValidator
from ...services.trasformators.parsers import IDParser

class ProductService:
    
    @staticmethod
    def get_all_products(dbfilter: DBFilter) -> List[ProductOutSchema]:
        products = DataBaseHandler.get_all(Product, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(products)
        return products
    
    @staticmethod
    def get_products_by_ids(ids: str, dbfilter: DBFilter) -> List[ProductOutSchema]:
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        products = DataBaseHandler.get_by_ids(Product, parsed_ids, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(products)
        return products

    @staticmethod
    def create_product(product: ProductInSchema) -> int:
        product_obj, is_created = DataBaseHandler.try_to_create(
            Product, product
        )
        DBValidator.is_created_or_already_exist(is_created, product_obj)
        status_code = 201
        return status_code
    