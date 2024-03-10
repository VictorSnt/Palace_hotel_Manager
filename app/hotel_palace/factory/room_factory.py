import factory
from ..models import Room, Category
from .category_factory import CategoryFactory
from ..utils.enums.room_status import RoomStatus


class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room

    number = factory.Sequence(lambda n: f'{n:03d}')
    status = factory.Iterator([s.value for s in RoomStatus])
    category = factory.LazyAttribute(
        lambda o: Category.objects.first() or CategoryFactory()
    )
