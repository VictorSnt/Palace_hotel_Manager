from datetime import date
from uuid import UUID
from ninja import Schema

class BaseCustomerSchema(Schema):
    full_name: str
    birth_date: date
    cpf: str
    rg: str
    gender: str
    marital_status: str
    partner: str
    occupation: str
    occupation_company_name: str
    zip_code: str
    address_street: str
    address_number: str
    address_ref: str
    address_district: str
    address_city: str
    address_uf: str
    phone: str
    cellphone: str
    email: str
    

class CustomerOutSchema(BaseCustomerSchema):
    id: UUID

class CustomerInSchema(BaseCustomerSchema):
    pass
