import factory
from ..models import Room, Category
from ..utils.enums.room_status import RoomStatus

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    
    description = factory.Sequence(lambda n: f'categoria_{n}')
    one_guest_price = 90
    two_guest_price = 170
    three_guest_price = 250
    four_guest_price = 300
    