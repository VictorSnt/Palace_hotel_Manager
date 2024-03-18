from typing import List
from ...database.handlers.database_handler import DataBaseHandler
from ...models import Accommodation, Consume, Product, Room
from ...schemas.models.consume_schema import (
    ConsumeInSchema, ConsumeOutSchema
)
from ...schemas.reponses.success_schemas import SuccessDetailed
from ...schemas.query_strings.database_filter import DBFilter
from ...services.base_service import BaseService


class ConsumeService(BaseService):
    
    ConsumeList = List[ConsumeOutSchema]
    Success201  = tuple[int, SuccessDetailed]
    
    @staticmethod
    def get_all(dbfilter: DBFilter) -> ConsumeList:
        ConsumeService._validate_db_field(Consume, dbfilter) 
        prod_consume = DataBaseHandler.get_all(Consume, dbfilter)
        ConsumeService._validate_queryset(prod_consume)
        return prod_consume
        
    @staticmethod
    def get_by_ids(ids: str, dbfilter: DBFilter) -> ConsumeList:
        ConsumeService._validate_db_field(Consume, dbfilter) 
        ids = ConsumeService._validate_n_parse_uuid(ids)
        prod_consume = DataBaseHandler.get_by_ids(Consume, ids, dbfilter)
        ConsumeService._validate_queryset(prod_consume)
        return prod_consume

    
    @staticmethod
    def create(consume: ConsumeInSchema) -> Success201:
        foreing_keys = [
            ('accommodation', Accommodation), 
            ('product', Product),
            ('room', Room)
        ]
        consume_dict = consume.model_dump()
        for attribute, model in foreing_keys:
            ids = ConsumeService._validate_n_parse_uuid(consume_dict[attribute])
            obj = DataBaseHandler.get_by_ids(model, ids)
            ConsumeService._validate_queryset(obj)
            consume_dict[attribute] = obj.first()
        response = DataBaseHandler.try_to_create(Consume, consume_dict)
        ConsumeService._validate_obj_creation(response)
        return 201, {'message': 'Criado com sucesso'}
