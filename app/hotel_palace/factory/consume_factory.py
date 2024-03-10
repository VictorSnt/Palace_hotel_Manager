import factory
from .accommodation_factory import AccommodationFactory
from .product_factory import ProductFactory
from .room_factory import RoomFactory
from ..models import Consume, Accommodation, Room, Product


class ConsumeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Consume
    
    accommodation = factory.LazyAttribute(
        lambda o: Accommodation.objects.first() or AccommodationFactory()
    )
    room = factory.LazyAttribute(
        lambda o: Room.objects.first() or RoomFactory()
    )
    product = factory.LazyAttribute(
        lambda o: Product.objects.first() or ProductFactory()
    )
    quantity = factory.Faker('random_int', min=1, max=10)
    unit_price = factory.Faker('random_number', digits=2, fix_len=True)
    total = factory.Faker('random_number', digits=2, fix_len=True)
