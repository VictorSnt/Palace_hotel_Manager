from django.shortcuts import get_object_or_404
from ninja_schema import ModelSchema, model_validator
from ...models import Accommodation, Room, Customer
from ...services.controller_services.accommodation_service import (
    AccommodationService
)


class CreateAccommodationSchema(ModelSchema):
    class Config:
        model = Accommodation
        include = [
            'room', 'customer',
            'guest_quant', 'checkin_date'
        ]
    
    def model_dump(self, *args, **kwargs):
        schema_dict: dict = super().model_dump(*args, **kwargs)
        customer_id = schema_dict.get('customer')
        room_id = schema_dict.get('room')
        if customer_id and room_id:
            customer_instance = get_object_or_404(Customer, pk=customer_id)
            room_instance = get_object_or_404(Room, pk=room_id)
            schema_dict['customer'] = customer_instance
            schema_dict['room'] = room_instance
            AccommodationService._validate_room(schema_dict['room'])
        AccommodationService._define_dates(schema_dict)
        AccommodationService._calc_hosting_price(schema_dict)
        return schema_dict
     
    @model_validator('guest_quant')
    def validate_enum(cls, enum):
        return enum.value if enum else None  
    
class UpdateAccommodationSchema(ModelSchema):
    class Config:
        model = Accommodation
        include = [
            'guest_quant', 'checkin_date', 'room', 'customer'
        ]
        optional = '__all__'
        
    @model_validator('guest_quant')
    def validate_enum(cls, enum):
        return enum.value if enum else None  
    
    
        
class AccommodationOutSchema(ModelSchema):
    class Config:
        model = Accommodation
        include = [
            'id', 'room',
            'customer', 'guest_quant',
            'days_quant', 'is_active',
            'checkin_date','checkin_time',
            'checkout_date', 'checkout_time',
            'hosting_price', 'total_hosting_price',
            'total_bill'
        ]
    