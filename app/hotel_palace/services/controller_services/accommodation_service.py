from datetime import datetime, time, timedelta
from decimal import ROUND_UP, Decimal

from ninja import Schema

from ...database.handlers.database_handler import DataBaseHandler
from ...services.errors.error_payload_generator import ErrorPayloadGenerator
from ...services.base_service import BaseService
from ..errors.exceptions import ValidationError
from ...models import Accommodation, Room


class AccommodationService(BaseService):
    
    def update(model, id, update_schema: Schema):
        current_obj = model.objects.get(pk=id)
        obj_dict = update_schema.model_dump()
        if not obj_dict.get('checkin_date'):
            obj_dict['checkin_date'] = current_obj.checkin_date
        obj_dict['checkout_date'] = current_obj.checkout_date
        obj_dict['room'] = current_obj.room
        AccommodationService._calc_hosting_price(obj_dict)
        DataBaseHandler.update(current_obj, obj_dict)
        return 200, {'detail': 'updated with success'}
    
    @staticmethod
    def delete(model, id):
        obj: Accommodation = DataBaseHandler.get_by_id(model, id)
        room = obj.room
        room.status = "Livre"
        room.save()
        obj.is_active = False
        obj.save()
        return 200, {'message': 'Deletado com sucesso'}  
     
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
        category = obj.get('room').category
        
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
        last_accommodation = room.accommodations.filter(is_active=True)
        if last_accommodation.exists() or room.status != "Livre":
            ErrorPayloadGenerator.generate_422_error_detailed(
                exc=ValidationError,
                status_code=400,
                type='NotValidParams',
                title='Reservation conflict',
                detail='Ja existe alguem hospedado nesse quarto',
            )