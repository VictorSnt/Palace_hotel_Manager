from django.shortcuts import get_object_or_404
from ninja_schema import ModelSchema
from ...models import Reservation, Room
from ...services.controller_services.reservation_service import (
    ReservationService
)


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
    
    def model_dump(self, *args, **kwargs):
        schema_dict = super().model_dump(*args, **kwargs)
        category_id = schema_dict.get('room')
        instance = get_object_or_404(Room, pk=category_id)
        schema_dict['room'] = instance
        ReservationService._validate_reservation(schema_dict)
        return schema_dict
