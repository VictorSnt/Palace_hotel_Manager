from typing import List
from ...database.handlers.database_handler import DataBaseHandler
from ...models import Reservation, Room
from ...schemas.models.reservation_schema import (
    ReservationInSchema, ReservationOutSchema
)
from ...schemas.query_strings.database_filter import DBFilter
from ...validators.id_validator import IDValidator
from ...validators.db_validators import DBValidator
from ...services.trasformators.parsers import IDParser

class ReservationService:
    
    @staticmethod
    def get_all_reservations(dbfilter: DBFilter) -> List[ReservationOutSchema]:
        DBValidator.is_valid_db_field(Reservation, dbfilter.order_by)  
        reservations = DataBaseHandler.get_all(Reservation, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(reservations)
        return reservations
    
    @staticmethod
    def get_reservations_by_ids(ids: str, dbfilter: DBFilter) -> List[ReservationOutSchema]:
        DBValidator.is_valid_db_field(Reservation, dbfilter.order_by)  
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        reservations = DataBaseHandler.get_by_ids(Reservation, parsed_ids, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(reservations)
        return reservations

    @staticmethod
    def create_reservation(reservation: ReservationInSchema) -> int:
        parsed_id = IDParser.paser_ids_by_comma(reservation.room)
        IDValidator.is_valid_uuid(parsed_id, param_name='room')
        room = DataBaseHandler.get_by_ids(Room, parsed_id)
        reservation_dict = reservation.model_dump()
        reservation_dict['room'] = room.first()
        reservation_obj, is_created = DataBaseHandler.try_to_create(
            Reservation, reservation_dict
        )
        DBValidator.is_created_or_already_exist(is_created, reservation_obj)
        return 201
    