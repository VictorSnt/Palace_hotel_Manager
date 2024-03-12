from typing import List
from ...database.handlers.database_handler import DataBaseHandler
from ...models import Accommodation, Consume, Product, Room
from ...schemas.models.consume_schema import (
    ConsumeInSchema, ConsumeOutSchema
)
from ...schemas.query_strings.database_filter import DBFilter
from ...validators.id_validator import IDValidator
from ...validators.db_validators import DBValidator
from ..trasformators.parsers import IDParser

class ConsumeService:
    
    @staticmethod
    def get_all_consumes(dbfilter: DBFilter) -> List[ConsumeOutSchema]:
        DBValidator.is_valid_db_field(Consume, dbfilter.order_by)  
        prod_consume = DataBaseHandler.get_all(Consume, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(prod_consume)
        return prod_consume
    
    @staticmethod
    def get_consumes_by_ids(ids: str, dbfilter: DBFilter) -> List[ConsumeOutSchema]:
        DBValidator.is_valid_db_field(Consume, dbfilter.order_by)  
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        prod_consume = DataBaseHandler.get_by_ids(Consume, parsed_ids, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(prod_consume)
        return prod_consume
    
    @staticmethod
    def create_consume(consume: ConsumeInSchema) -> int:
        foreing_keys = [
            ('accommodation', Accommodation), 
            ('product', Product),
            ('room', Room)
        ]
        consume_dict = consume.model_dump()
        for attribute, model in foreing_keys:
            parsed_id = IDParser.paser_ids_by_comma(
                consume_dict[attribute]
            )
            IDValidator.is_valid_uuid(parsed_id, param_name=attribute)
            obj = DataBaseHandler.get_by_ids(model, parsed_id)
            DBValidator.is_valid_and_not_empty_queryset(obj)
            consume_dict[attribute] = obj.first()

        consume_obj, is_created = DataBaseHandler.try_to_create(
            Consume, consume_dict
        )
        DBValidator.is_created_or_already_exist(is_created, consume_obj)
        return 201
