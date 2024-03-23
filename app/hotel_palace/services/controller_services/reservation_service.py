from ninja import Schema
from ...services.errors.error_payload_generator import ErrorPayloadGenerator
from ...models import Reservation
from ...schemas.reponses.success_schemas import SuccessDetailed
from ...services.base_service import BaseService
from ...services.errors.exceptions import ValidationError

class ReservationService(BaseService):
    
    Success201  = tuple[int, SuccessDetailed]

    @staticmethod
    def _validate_reservation(reserv_schema: dict):
        try:
            room = reserv_schema['room']
            query = {'checkin_date': reserv_schema.checkin_date}
            reserv = Reservation.objects.get(**query)
            if reserv.room.number == room.number:
                ErrorPayloadGenerator.generate_422_error_detailed(
                exc=ValidationError,
                status_code=409,
                type='NotValidParams',
                title='Reservation conflict',
                detail='Ja existe reserva para o mesmo quarto na mesma data',
            )
        except Reservation.DoesNotExist:
            return
        