from ninja import ModelSchema
from ..models import Customer

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
