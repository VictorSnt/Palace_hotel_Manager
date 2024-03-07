from typing import List
from ...database.handlers.database_handler import DataBaseHandler
from ...models import Customer
from ...schemas.customer_schema import CustomerSchema
from ...schemas.database_filter import DBFilter
from ...validators.id_validator import IDValidator
from ...validators.db_validators import DBValidator
from ...services.trasformators.parsers import IDParser

class CustomerService:
    
    @staticmethod
    def get_all_customers(dbfilter: DBFilter) -> List[CustomerSchema]:
        customers = DataBaseHandler.get_all(Customer, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(customers)
        return customers
    
    @staticmethod
    def get_customers_by_ids(ids: str, dbfilter: DBFilter) -> List[CustomerSchema]:
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        customers = DataBaseHandler.get_by_ids(Customer, parsed_ids, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(customers)
        return customers