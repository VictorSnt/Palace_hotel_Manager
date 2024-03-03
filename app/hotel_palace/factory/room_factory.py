import factory
from ..models import Room, RoomCategory
from ..enums.room_status import RoomStatus

class RoomCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RoomCategory

    description = factory.Faker('word')
    one_guest_price = factory.Faker('random_number', digits=3)
    two_guest_price = factory.Faker('random_number', digits=3)
    three_guest_price = factory.Faker('random_number', digits=3)
    four_guest_price = factory.Faker('random_number', digits=3)


class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room

    room_number = factory.Sequence(lambda n: f'{n:03d}')
    status = factory.Iterator([s.value for s in RoomStatus])
    category = factory.SubFactory(RoomCategoryFactory)