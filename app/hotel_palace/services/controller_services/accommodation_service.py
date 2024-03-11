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


class AccommodationService:
    
    @staticmethod
    def get_all_accommodations(
        dbfilter: DBFilter) -> List[AccommodationOutSchema]:
        
        accommodations = DataBaseHandler.get_all(Accommodation, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(accommodations)
        return accommodations
    
    @staticmethod
    def get_accommodations_by_ids(
        ids: str, dbfilter: DBFilter) -> List[AccommodationOutSchema]:
        
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        
        accommodations = DataBaseHandler.get_by_ids(
            Accommodation, parsed_ids, dbfilter)
        
        DBValidator.is_valid_and_not_empty_queryset(accommodations)
        return accommodations
    
    @staticmethod
    def create_accommodation(accommodation: AccommodationInSchema) -> int:
        foreing_keys = [
            ('room', Room), 
            ('customer', Customer)
        ]
        for attribute, model in foreing_keys:
            parsed_id = IDParser.paser_ids_by_comma(
                getattr(accommodation, attribute)
            )
            IDValidator.is_valid_uuid(parsed_id, param_name=attribute)
            obj = DataBaseHandler.get_by_ids(model, parsed_id)
            DBValidator.is_valid_and_not_empty_queryset(obj)
            setattr(accommodation, attribute, obj.first())

        accommodation_obj, is_created = DataBaseHandler.try_to_create(
            Accommodation, accommodation
        )
        DBValidator.is_created_or_already_exist(is_created, accommodation_obj)
        return 201
    