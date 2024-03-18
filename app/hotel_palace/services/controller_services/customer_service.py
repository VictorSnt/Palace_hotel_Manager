from typing import List
from ...database.handlers.database_handler import DataBaseHandler
from ...models import Customer
from ...schemas.models.customer_schema import (
    CustomerInSchema, CustomerOutSchema
)
from ...utils.enums.marital_status import MaritalStatus
from ...utils.enums.brazilian_states import BrazilianStates
from ...utils.enums.gender import Gender
from ...schemas.query_strings.database_filter import DBFilter
from ...schemas.reponses.success_schemas import SuccessDetailed
from ...validators.id_validator import IDValidator
from ...validators.db_validators import DBValidator
from ...validators.enum_validator import EnumValidator
from ...services.trasformators.parsers import IDParser
from ...services.base_service import BaseService


class CustomerService(BaseService):
    
    CostumerList = List[CustomerOutSchema]
    Success201  = tuple[int, SuccessDetailed]
    
    @staticmethod
    def get_all(dbfilter: DBFilter) -> CostumerList:
        
        CustomerService._validate_db_field(Customer, dbfilter) 
        customers = DataBaseHandler.get_all(Customer, dbfilter)
        CustomerService._validate_queryset(customers)
        return customers
    
    @staticmethod
    def get_by_ids(ids: str, dbfilter: DBFilter) -> CostumerList:
        
        CustomerService._validate_db_field(Customer, dbfilter) 
        ids = CustomerService._validate_n_parse_uuid(ids)
        customers = DataBaseHandler.get_by_ids(Customer, ids, dbfilter)
        CustomerService._validate_queryset(customers)
        return customers
    
    @staticmethod
    def create(customer: CustomerInSchema) -> Success201:
        
        enums_list = [
            (Gender, customer.gender, 'gender'), 
            (BrazilianStates, customer.address_uf, 'address_uf'), 
            (MaritalStatus, customer.marital_status, 'marital_status')
        ]
        for enum, value, attr in enums_list:
            CustomerService._validate_enum(enum, value, attr)
        
        args = Customer, customer.model_dump()
        response = DataBaseHandler.try_to_create(*args)
        CustomerService._validate_obj_creation(response)
        return 201, {'message': 'Criado com sucesso'}
    