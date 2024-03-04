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
    full_name = fake.name()
    birth_date = fake.date_of_birth()
    cpf = fake.cpf()
    rg = fake.rg()
    gender = factory.Faker('random_element', elements=[gender.value for gender in Gender])
    marital_status = factory.Faker('random_element', elements=[status.value for status in MaritalStatus])
    partner = fake.name()
    occupation = fake.job()
    occupation_company_name = fake.company()
    zip_code = fake.postcode()
    address_street = fake.street_name()
    address_number = fake.building_number()
    address_ref = fake.random_int(min=1, max=999)
    address_district = fake.neighborhood()
    address_city = fake.city()
    address_uf = factory.Faker('random_element', elements=[state.value for state in BrazilianStates])
    phone = fake.phone_number()
    cellphone = fake.phone_number()
    email = fake.email()
