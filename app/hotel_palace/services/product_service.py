from typing import List
from ..database.handlers.database_handler import DataBaseHandler
from ..models import Product
from ..schemas.products_schema import ProductsSchema
from ..schemas.database_filter import DBFilter
from ..validators.id_validator import IDValidator
from ..validators.db_validators import DBValidator
from ..services.parsers import IDParser

class ProductService:
    
    @staticmethod
    def get_all_products(dbfilter: DBFilter) -> List[ProductsSchema]:
        products = DataBaseHandler.get_all(Product, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(products)
        return products
    
    @staticmethod
    def get_products_by_ids(ids: str, dbfilter: DBFilter) -> List[ProductsSchema]:
        IDValidator.is_valid_id_type(ids)
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        products = DataBaseHandler.get_by_ids(Product, parsed_ids, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(products)
        return products
