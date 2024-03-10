import factory
from django.utils.functional import SimpleLazyObject
from ..utils.enums.guest_quantity import GuestQuantity
from .room_factory import RoomFactory
from .customer_factory import CustomerFactory
from ..models import Accommodation, Room, Customer

class AccommodationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Accommodation
    
    room = factory.LazyAttribute(
        lambda o: Room.objects.first() or RoomFactory()
    )
    customer = factory.LazyAttribute(
        lambda o: Customer.objects.first() or CustomerFactory()
    )
    guest_quant = factory.Faker(
        'random_element', elements=[s.value for s in GuestQuantity]
    )
    is_active = True
    days_quant = factory.Faker('random_int', min=1, max=10)
    checkin_date = factory.Faker('date_this_year')
    checkout_date = factory.Faker('date_between', start_date=checkin_date)
    checkin_time = factory.Faker('time', end_datetime=checkin_date)
    checkout_time = factory.Faker('time', end_datetime=checkout_date)
    hosting_price = factory.Faker('random_number', digits=2, fix_len=True)
    total_hosting_price = factory.Faker(
        'random_number', digits=2, fix_len=True
    )
    total_bill = factory.Faker('random_number', digits=2, fix_len=True)
