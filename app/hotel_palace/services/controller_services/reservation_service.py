from typing import List
from ...database.handlers.database_handler import DataBaseHandler
from ...models import Reservation
from ...schemas.models.reservation_schema import ReservationSchema
from ...schemas.query_strings.database_filter import DBFilter
from ...validators.id_validator import IDValidator
from ...validators.db_validators import DBValidator
from ...services.trasformators.parsers import IDParser

class ReservationService:
    
    @staticmethod
    def get_all_reservations(dbfilter: DBFilter) -> List[ReservationSchema]:
        reservations = DataBaseHandler.get_all(Reservation, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(reservations)
        return reservations
    
    @staticmethod
    def get_reservations_by_ids(ids: str, dbfilter: DBFilter) -> List[ReservationSchema]:
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        reservations = DataBaseHandler.get_by_ids(Reservation, parsed_ids, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(reservations)
        return reservations
