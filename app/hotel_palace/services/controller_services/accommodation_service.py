from typing import List
from ...database.handlers.database_handler import DataBaseHandler
from ...models import Accommodation, Customer, Room
from ...schemas.models.accomodation_schema import (
    AccommodationInSchema, AccommodationOutSchema
)
from ...schemas.query_strings.database_filter import DBFilter
from ...validators.id_validator import IDValidator
from ...validators.db_validators import DBValidator
from ...services.trasformators.parsers import IDParser
from ...services.base_service import BaseService


class AccommodationService(BaseService):
    
    AccommodationList = List[AccommodationOutSchema]
    
    @staticmethod
    def get_all(dbfilter: DBFilter) -> AccommodationList:
        AccommodationService._validate_db_field(Accommodation, dbfilter) 
        accommodations = DataBaseHandler.get_all(Accommodation, dbfilter)
        AccommodationService._validate_queryset(accommodations)
        return accommodations
    
    @staticmethod
    def get_by_ids(ids: str, dbfilter: DBFilter) -> AccommodationList:
        AccommodationService._validate_db_field(Accommodation, dbfilter) 
        ids = AccommodationService._validate_n_parse_uuid(ids)
        args = (Accommodation, ids, dbfilter)
        accommodations = DataBaseHandler.get_by_ids(*args)
        AccommodationService._validate_queryset(accommodations)
        return accommodations
    
    @staticmethod
    def create(accommodation: AccommodationInSchema) -> int:
        foreing_keys = [
            ('room', Room), 
            ('customer', Customer)
        ]
        accommodations_dict = accommodation.model_dump()
        for attribute, model in foreing_keys:
            attr_id = accommodations_dict[attribute]
            ids = AccommodationService._validate_n_parse_uuid(attr_id)
            obj = DataBaseHandler.get_by_ids(model, ids)
            AccommodationService._validate_queryset(obj)
            accommodations_dict[attribute] = obj.first()
        response = DataBaseHandler.try_to_create(Accommodation, accommodations_dict)
        AccommodationService._validate_obj_creation(response)
        return 201, {'message': 'Criado com sucesso'}
    