import factory
import uuid
from faker import Faker
from ..models import Customer
from ..utils.enums.brazilian_states import BrazilianStates
from ..utils.enums.marital_status import MaritalStatus
from ..utils.enums.gender import Gender

fake = Faker('pt_BR')

class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer
    
    id = factory.LazyFunction(uuid.uuid4)
    full_name = factory.LazyAttribute(lambda x: fake.name()[:100])
    birth_date = factory.LazyAttribute(lambda x: fake.date_of_birth())
    cpf = factory.LazyAttribute(lambda x: fake.cpf()[:14])
    rg = factory.LazyAttribute(lambda x: fake.rg()[:9])
    gender = factory.Faker('random_element', elements=[gender.value for gender in Gender])
    marital_status = factory.Faker('random_element', elements=[status.value for status in MaritalStatus])
    partner = factory.LazyAttribute(lambda x: fake.name()[:100])
    occupation = factory.LazyAttribute(lambda x: fake.job()[:25])
    occupation_company_name = factory.LazyAttribute(lambda x: fake.company()[:25])
    zip_code = factory.LazyAttribute(lambda x: fake.postcode()[:25])
    address_street = factory.LazyAttribute(lambda x: fake.street_name()[:50])
    address_number = factory.LazyAttribute(lambda x: fake.building_number()[:6])
    address_ref = factory.LazyAttribute(lambda x: str(fake.random_int(min=1, max=999))[:25])
    address_district = factory.LazyAttribute(lambda x: fake.neighborhood()[:50])
    address_city = factory.LazyAttribute(lambda x: fake.city()[:20])
    address_uf = factory.Faker('random_element', elements=[state.value for state in BrazilianStates])
    phone = factory.LazyAttribute(lambda x: fake.phone_number()[:21])
    cellphone = factory.LazyAttribute(lambda x: fake.phone_number()[:21])
    email = factory.LazyAttribute(lambda x: fake.email()[:254])
