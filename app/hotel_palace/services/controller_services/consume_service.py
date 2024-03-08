from typing import List
from ...database.handlers.database_handler import DataBaseHandler
from ...models import Consume
from ...schemas.models.consume_schema import ConsumeSchema
from ...schemas.query_strings.database_filter import DBFilter
from ...validators.id_validator import IDValidator
from ...validators.db_validators import DBValidator
from ..trasformators.parsers import IDParser

class ConsumeService:
    
    @staticmethod
    def get_all_consumes(dbfilter: DBFilter) -> List[ConsumeSchema]:
        prod_consume = DataBaseHandler.get_all(Consume, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(prod_consume)
        return prod_consume
    
    @staticmethod
    def get_consumes_by_ids(ids: str, dbfilter: DBFilter) -> List[ConsumeSchema]:
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        prod_consume = DataBaseHandler.get_by_ids(Consume, parsed_ids, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(prod_consume)
        return prod_consume
