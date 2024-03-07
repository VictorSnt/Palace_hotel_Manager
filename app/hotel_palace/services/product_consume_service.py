from typing import List
from ..database.handlers.database_handler import DataBaseHandler
from ..models import ProductConsume
from ..schemas.product_consume_schema import ProductConsumeSchema
from ..schemas.database_filter import DBFilter
from ..validators.id_validator import IDValidator
from ..validators.db_validators import DBValidator
from ..services.parsers import IDParser

class ProductConsumeService:
    
    @staticmethod
    def get_all_consumes(dbfilter: DBFilter) -> List[ProductConsumeSchema]:
        prod_consume = DataBaseHandler.get_all(ProductConsume, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(prod_consume)
        return prod_consume
    
    @staticmethod
    def get_consumes_by_ids(ids: str, dbfilter: DBFilter) -> List[ProductConsumeSchema]:
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        prod_consume = DataBaseHandler.get_by_ids(ProductConsume, parsed_ids, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(prod_consume)
        return prod_consume
