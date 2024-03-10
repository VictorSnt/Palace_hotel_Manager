from ninja import ModelSchema
from ...models import Customer

class CustomerSchema(ModelSchema):
    class Config:
        model = Customer
        model_fields = [
            "id", "full_name", "birth_date", "cpf",
            "rg", "gender", "marital_status",
            "partner", "occupation", "occupation_company_name",
            "zip_code", "address_street", "address_number",
            "address_ref", "address_district", "address_city",
            "address_uf", "phone", "cellphone", "email",
        ]

from uuid import UUID
from ninja import Schema

class BaseRoomSchema(Schema):
    full_name: str
    birth_date: str
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
    
    
    

class RoomOutSchema(BaseRoomSchema):
    id: UUID

class RoomInSchema(BaseRoomSchema):
    category: str
