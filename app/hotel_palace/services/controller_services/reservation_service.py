from typing import List

from django.db.models import Model
from ...database.handlers.database_handler import DataBaseHandler
from ...models import Reservation, Room
from ...schemas.models.reservation_schema import (
    ReservationInSchema, ReservationOutSchema
)
from ...schemas.reponses.success_schemas import SuccessDetailed
from ...schemas.query_strings.database_filter import DBFilter
from ...validators.id_validator import IDValidator
from ...validators.db_validators import DBValidator
from ...services.trasformators.parsers import IDParser

class ReservationService:
    
    ReservationList = List[ReservationOutSchema]
    Success201  = tuple[int, SuccessDetailed]
    
    @staticmethod
    def get_all(dbfilter: DBFilter) -> ReservationList:
        ReservationService._validate_db_field(dbfilter)
        reservations = DataBaseHandler.get_all(Reservation, dbfilter)
        ReservationService._validate_queryset(reservations)
        return reservations
    
    @staticmethod
    def get_by_ids(ids: str, dbfilter: DBFilter) -> ReservationList:
        ReservationService._validate_db_field(dbfilter)
        parsed_ids = ReservationService._validate_uuid(ids)
        args = Reservation, parsed_ids, dbfilter
        reservations = DataBaseHandler.get_by_ids(*args)
        ReservationService._validate_queryset(reservations)
        return reservations

    @staticmethod
    def create(reservation: ReservationInSchema) -> Success201:
        parsed_room_id = ReservationService._parse_room_id(reservation.room)
        room = ReservationService._get_room_by_id(parsed_room_id)
        reservation_dict = ReservationService._parse_schema(reservation, room)
        response = DataBaseHandler.try_to_create(Reservation, reservation_dict)
        ReservationService._validate_obj_creation(response)
        return 201, {'message': 'Criado com sucesso'}
    
    @staticmethod
    def _validate_db_field(dbfilter: DBFilter) -> None:
        DBValidator.is_valid_db_field(Reservation, dbfilter.order_by)
    
    @staticmethod
    def _validate_queryset(reservations: ReservationList) -> None:
        DBValidator.is_valid_and_not_empty_queryset(reservations)
    
    @staticmethod
    def _validate_uuid(ids: str) -> str:
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        return parsed_ids
    
    @staticmethod
    def _parse_room_id(room_id: str) -> str:
        parsed_room_id = IDParser.paser_ids_by_comma(room_id)
        IDValidator.is_valid_uuid(parsed_room_id, param_name='room')
        return parsed_room_id
    
    @staticmethod
    def _get_room_by_id(room_id: str) -> Room:
        room = DataBaseHandler.get_by_ids(Room, room_id)
        ReservationService._validate_queryset(room)
        return room.first()
    
    @staticmethod
    def _parse_schema(reservation: ReservationInSchema, room: Room) -> dict:
        reservation_dict = reservation.model_dump()
        reservation_dict['room'] = room
        return reservation_dict
    
    @staticmethod
    def _validate_obj_creation(response: tuple[bool, Model]) -> None:
        room_obj, is_created = response
        DBValidator.is_created_or_already_exist(is_created, room_obj)
