import factory
from ..models import Product

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    
    description = factory.Faker('word')
    price = factory.Faker('random_number', digits=3)
    