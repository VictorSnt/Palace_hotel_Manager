import factory
from ..models import Room, RoomCategory
from ..utils.enums.room_status import RoomStatus

class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room

    number = factory.Sequence(lambda n: f'{n:03d}')
    status = factory.Iterator([s.value for s in RoomStatus])
    category = RoomCategory.objects.get_or_create(
        description='padrão', one_guest_price=90, two_guest_price=170, 
        three_guest_price=250, four_guest_price=300
    )[0]
    
