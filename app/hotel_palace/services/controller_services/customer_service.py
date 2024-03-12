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
from ...validators.id_validator import IDValidator
from ...validators.db_validators import DBValidator
from ...validators.enum_validator import EnumValidator
from ...services.trasformators.parsers import IDParser

class CustomerService:
    
    @staticmethod
    def get_all_customers(
        dbfilter: DBFilter
        ) -> List[CustomerOutSchema]:
        
        DBValidator.is_valid_db_field(Customer, dbfilter.order_by)  
        customers = DataBaseHandler.get_all(Customer, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(customers)
        return customers
    
    @staticmethod
    def get_customers_by_ids(
        ids: str, dbfilter: DBFilter
        ) -> List[CustomerOutSchema]:
        
        DBValidator.is_valid_db_field(Customer, dbfilter.order_by)  
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        customers = DataBaseHandler.get_by_ids(Customer, parsed_ids, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(customers)
        return customers
    
    @staticmethod
    def create_customer(customer: CustomerInSchema) -> int:
        gender = customer.gender
        address_uf = customer.address_uf
        marital_status = customer.marital_status
        EnumValidator.validate_enum(Gender, gender, 'gender')
        EnumValidator.validate_enum(BrazilianStates, address_uf, 'address_uf')
        EnumValidator.validate_enum(
            MaritalStatus, marital_status, 'marital_status'
        )
        customer_obj, is_created = DataBaseHandler.try_to_create(
            Customer, customer.model_dump()
        )
        DBValidator.is_created_or_already_exist(is_created, customer_obj)
        status_code = 201
        return status_code
    