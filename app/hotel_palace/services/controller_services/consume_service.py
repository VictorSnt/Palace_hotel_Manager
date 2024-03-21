from typing import List

from ...database.handlers.database_handler import DataBaseHandler
from ...models import Accommodation, Consume, Product
from ...schemas.models.consume_schema import (
    ConsumeInSchema, ConsumeOutSchema
)
from ...schemas.reponses.success_schemas import SuccessDetailed
from ...schemas.query_strings.database_filter import DBFilter
from ...services.base_service import BaseService


class ConsumeService(BaseService):
    
    ConsumeList = List[ConsumeOutSchema]
    Success201  = tuple[int, SuccessDetailed]
    foreing_keys = [
            ('accommodation', Accommodation), 
            ('product', Product)
        ]
    
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
        consume_dict = ConsumeService._parse_data(consume, ConsumeService)
        ConsumeService._parse_product_info(consume_dict)
        ConsumeService._parse_accommodation_info(consume_dict)
        DataBaseHandler.try_to_create(Consume, consume_dict, allow_dups=True)
        return 201, {'message': 'Criado com sucesso'}
    
    @staticmethod
    def _parse_product_info(obj: dict):
        obj['unit_price'] = obj['product'].price
        obj['total'] = obj['product'].price * obj['quantity']
        
    @staticmethod
    def _parse_accommodation_info(obj: dict):
        total_bill = float(obj['accommodation'].total_bill)
        total_bill += obj['total']
        obj['accommodation'].total_bill = total_bill
        obj['accommodation'].save()
        
    