from datetime import datetime
import json
from django.shortcuts import get_object_or_404
from ninja_schema import ModelSchema, model_validator
from ...services.controller_services.reservation_service import (
    ReservationService
)
from ...models import Reservation, Room
from ...services.errors.exceptions import ValidationError


class ReservationOutSchema(ModelSchema):
    class Config:
        model = Reservation
        include = [
            'id', 'room', 
            'checkin_date', 'customer_name'
        ]


class CreateReservationSchema(ModelSchema):
    class Config:
        model = Reservation
        include = [
            'room', 
            'checkin_date', 
            'customer_name'
        ]
    
    @model_validator('checkin_date')
    def validate_checkin_date(cls, checkin_date):
        if datetime.now().date() > checkin_date:
            msg = json.dumps({'detail': 'O checkin não pode ser retroativo'})
            raise ValidationError(msg, 422)

    @model_validator('customer_name')
    def validate_customer_name(cls, customer_name):
        if len(customer_name) < 3:
            msg = json.dumps({'detail': 'O nome deve ter mais de 3 letras'})
            raise ValidationError(msg, 422)
        return customer_name
        
    def model_dump(self, *args, **kwargs):
        schema_dict = super().model_dump(*args, **kwargs)
        room_id = schema_dict.get('room', False)
        if room_id:
            instance = get_object_or_404(Room, pk=room_id)
            schema_dict['room'] = instance
            ReservationService._validate_reservation(schema_dict)
        return schema_dict

class UpdateReservationSchema(ModelSchema):
    class Config:
        model = Reservation
        include = [
            'room', 
            'checkin_date', 
            'customer_name'
        ]
        
        optional = [
            'room', 
            'checkin_date', 
            'customer_name'
        ]
    
    