import factory
from django.utils.functional import SimpleLazyObject
from ..models import Reservation, Room
from .room_factory import RoomFactory

class ReservationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reservation

    room = factory.LazyAttribute(
        lambda o: Room.objects.first() or  RoomFactory()
    )
    checkin_date = factory.Faker('date_this_year')
    customer_name = factory.Faker('name')
