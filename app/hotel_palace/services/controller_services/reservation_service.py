from typing import List

from django.db.models import Model

from ...services.errors.error_payload_generator import ErrorPayloadGenerator
from ...database.handlers.database_handler import DataBaseHandler
from ...models import Reservation, Room
from ...schemas.models.reservation_schema import (
    ReservationInSchema, ReservationOutSchema
)
from ...schemas.reponses.success_schemas import SuccessDetailed
from ...schemas.query_strings.database_filter import DBFilter
from ...services.base_service import BaseService
from ...services.errors.exceptions import ValidationError

class ReservationService(BaseService):
    
    ReservationList = List[ReservationOutSchema]
    Success201  = tuple[int, SuccessDetailed]
    
    @staticmethod
    def get_all(dbfilter: DBFilter) -> ReservationList:
        ReservationService._validate_db_field(Reservation, dbfilter)
        reservations = DataBaseHandler.get_all(Reservation, dbfilter)
        ReservationService._validate_queryset(reservations)
        return reservations
    
    @staticmethod
    def get_by_ids(ids: str, dbfilter: DBFilter) -> ReservationList:
        ReservationService._validate_db_field(Reservation, dbfilter)
        parsed_ids = ReservationService._validate_n_parse_uuid(ids)
        args = Reservation, parsed_ids, dbfilter
        reservations = DataBaseHandler.get_by_ids(*args)
        ReservationService._validate_queryset(reservations)
        return reservations

    @staticmethod
    def create(reservation: ReservationInSchema) -> Success201:
        room_id = ReservationService._validate_n_parse_uuid(reservation.room)
        room = DataBaseHandler.get_by_ids(Room, room_id)
        ReservationService._validate_queryset(room)
        reservation_dict = ReservationService._parse_schema(reservation, room)
        ReservationService._validate_reservation(Reservation, reservation_dict)
        response = DataBaseHandler.try_to_create(Reservation, reservation_dict)
        ReservationService._validate_obj_creation(response)
        return 201, {'message': 'Criado com sucesso'}

    @staticmethod
    def _validate_reservation(model: Reservation, reserv_schema: dict):
        try:
            room = reserv_schema['room']
            query = {'checkin_date': reserv_schema['checkin_date']}
            reserv = model.objects.get(**query)
            if reserv.room.number == room.number:
                ErrorPayloadGenerator.generate_422_error_detailed(
                exc=ValidationError,
                status_code=422,
                type='NotValidParams',
                title='Reservation conflict',
                detail='Ja existe reserva para o mesmo quarto na mesma data',
            )
        except model.DoesNotExist:
            return
        