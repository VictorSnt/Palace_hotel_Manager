from datetime import datetime, time, timedelta
from decimal import ROUND_UP, Decimal
from ...services.errors.error_payload_generator import ErrorPayloadGenerator
from ...services.base_service import BaseService
from ..errors.exceptions import ValidationError
from ...models import Room


class AccommodationService(BaseService):
   
    @staticmethod
    def _define_dates(obj: dict):
        today_date = datetime.now().date()
        nows_time = datetime.now().time()
        if obj['checkin_date'] > today_date:
            raise ValidationError(
                'A data deve de entrada não ' 
                'pode ser posterior a data atual'
                ,422
            )
        obj['checkin_date'] = obj['checkin_date'] or datetime.now().date()
        obj['checkout_date'] = obj['checkin_date'] + timedelta(days=1)
        obj['checkin_time'] = nows_time
        obj['checkout_time'] = time(13,30)
        
    
    @staticmethod
    def _calc_hosting_price(obj: dict):
        if not 1 <= obj['guest_quant'] <= 4:
            raise ValidationError(
                'O quarto poder hospedar de 1 ate 4 pessoas' 
                f' ({obj["guest_quant"]}) é uma quantidade invalida'
                ,422
            )
        category = obj['room'].category
        
        if obj['guest_quant'] == 1:
            obj['hosting_price'] = category.one_guest_price
        
        elif obj['guest_quant'] == 2:
            obj['hosting_price'] = category.two_guest_price
        
        elif obj['guest_quant'] == 3:
            obj['hosting_price'] = category.three_guest_price
        
        else:
            obj['hosting_price'] = category.four_guest_price
            
        days_diff = (obj['checkout_date'] - obj['checkin_date']).days
        days_diff = Decimal(days_diff).quantize(
            Decimal('1.'), rounding=ROUND_UP)
        obj['days_quant'] = days_diff
        obj['total_hosting_price'] = obj['hosting_price'] * int(days_diff)
        obj['total_bill'] = obj['total_hosting_price']
        room = obj['room']
        room.status = 'OCCUPIED'
        room.save()
        obj['is_active'] = True
        
    
    @staticmethod
    def _validate_room(room: Room):
        last_accommodation = room.accommodations.order_by('-created_at')
        if last_accommodation.exists():
            accommodation_obj = last_accommodation.first()
            if accommodation_obj.is_active or room.status != "FREE":
                ErrorPayloadGenerator.generate_422_error_detailed(
                exc=ValidationError,
                status_code=400,
                type='NotValidParams',
                title='Reservation conflict',
                detail='Ja existe alguem hospedado nesse quarto',
            )