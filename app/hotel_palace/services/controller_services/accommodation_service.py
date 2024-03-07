from typing import List
from ...database.handlers.database_handler import DataBaseHandler
from ...models import Accommodation
from ...schemas.accomodation_schema import AccommodationSchema
from ...schemas.database_filter import DBFilter
from ...validators.id_validator import IDValidator
from ...validators.db_validators import DBValidator
from ...services.trasformators.parsers import IDParser


class AccommodationService:
    
    @staticmethod
    def get_all_accommodations(
        dbfilter: DBFilter) -> List[AccommodationSchema]:
        
        accommodations = DataBaseHandler.get_all(Accommodation, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(accommodations)
        return accommodations
    
    @staticmethod
    def get_accommodations_by_ids(
        ids: str, dbfilter: DBFilter) -> List[AccommodationSchema]:
        
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        
        accommodations = DataBaseHandler.get_by_ids(
            Accommodation, parsed_ids, dbfilter)
        
        DBValidator.is_valid_and_not_empty_queryset(accommodations)
        return accommodations
    