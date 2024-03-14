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

class CustomerService:
    
    CostumerList = List[CustomerOutSchema]
    Success201  = tuple[int, SuccessDetailed]
    
    @staticmethod
    def get_all(dbfilter: DBFilter) -> CostumerList:
        
        DBValidator.is_valid_db_field(Customer, dbfilter.order_by)  
        customers = DataBaseHandler.get_all(Customer, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(customers)
        return customers
    
    @staticmethod
    def get_by_ids(ids: str, dbfilter: DBFilter) -> CostumerList:
        
        DBValidator.is_valid_db_field(Customer, dbfilter.order_by)  
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        customers = DataBaseHandler.get_by_ids(Customer, parsed_ids, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(customers)
        return customers
    
    @staticmethod
    def create(customer: CustomerInSchema) -> Success201:
        gender = customer.gender
        address_uf = customer.address_uf
        marital_status = customer.marital_status
        EnumValidator.validate_enum(Gender, gender, 'gender')
        EnumValidator.validate_enum(BrazilianStates, address_uf, 'address_uf')
        args = MaritalStatus, marital_status, 'marital_status'
        EnumValidator.validate_enum(*args)
        args = Customer, customer.model_dump()
        customer_obj, is_created = DataBaseHandler.try_to_create(*args)
        DBValidator.is_created_or_already_exist(is_created, customer_obj)
        return 201, {'message': 'Criado com sucesso'}
    