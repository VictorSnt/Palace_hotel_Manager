from ninja import ModelSchema
from ..models import RoomAccommodation


class RoomAccommodationSchema(ModelSchema):
    class Config:
        model = RoomAccommodation
        model_fields = [
            "id", "room", "customer", "guest_quant", "is_active", "days_quant",
            "checkin_date", "checkout_date", "checkin_time", "checkout_time",
            "hosting_price", "total_hosting_price", "total_bill"
        ]