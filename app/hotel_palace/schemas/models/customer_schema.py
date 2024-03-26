from datetime import datetime, date, timedelta
import datetime
import json
import re
from ninja_schema import ModelSchema, model_validator
from ...models import Customer
from ...services.errors.exceptions import ValidationError

class CreateOrUpdateCustomerSchema(ModelSchema):
    
    class Config:
        model = Customer
        include = [
            'full_name', 'birth_date', 'cpf', 'rg', 
            'gender', 'marital_status', 'partner', 
            'occupation', 'occupation_company_name', 
            'zip_code', 'address_street', 'address_number', 
            'address_ref', 'address_district', 'address_city', 
            'address_uf', 'phone', 'cellphone', 'email'
        ]
        optional = [
            'full_name', 'birth_date', 'cpf', 'rg', 
            'gender', 'marital_status', 'partner', 
            'occupation', 'occupation_company_name', 
            'zip_code', 'address_street', 'address_number', 
            'address_ref', 'address_district', 'address_city', 
            'address_uf', 'phone', 'cellphone', 'email'
        ]
    
    @model_validator('gender', 'marital_status', 'address_uf')
    def validate_enum(cls, enum):
        return enum.value if enum else None
    
    
    @model_validator('birth_date')
    def validate_birth_date(cls, birth_date: date) -> date:
        eighteen_years_ago = datetime.datetime.now() - timedelta(days=18*365)
        if birth_date >= eighteen_years_ago.date():
            res = {'detail': 'O cliente deve ter pelo menos 18 anos'}
            json_res = json.dumps(res)
            raise ValidationError(json_res, 422)
        return birth_date

    @model_validator('cpf')
    def validate_cpf(cls, cpf: str) -> str:
        cpf = re.sub(r'\D', '', cpf) 
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            res = {'detail': 'CPF inválido'}
            json_res = json.dumps(res)
            raise ValidationError(json_res, 422)
        
    @model_validator('email')
    def validate_email(cls, email: str) -> str:
        if not re.match(r'^[\w\.-]+@[\w\.-]+(?:\.[\w]+)+$', email):
            res = {'detail': 'E-mail inválido'}
            json_res = json.dumps(res)
            raise ValidationError(json_res, 422)
        return email

    @model_validator('phone', 'cellphone')
    def validate_phone(cls, phone: str) -> str:
        phone = re.sub(r'\D', '', phone)
        if not re.match(r'^\d{10,11}$', phone):
            res = {'detail': 'Telefone inválido'}
            json_res = json.dumps(res)
            raise ValidationError(json_res, 422)
        return phone



class CustomerOutSchema(ModelSchema):
    class Config:
        model = Customer
        include = [
            'id', 'full_name', 'birth_date', 'cpf', 'rg', 
            'gender', 'marital_status', 'partner', 
            'occupation', 'occupation_company_name', 
            'zip_code', 'address_street', 'address_number', 
            'address_ref', 'address_district', 'address_city', 
            'address_uf', 'phone', 'cellphone', 'email'
        ]