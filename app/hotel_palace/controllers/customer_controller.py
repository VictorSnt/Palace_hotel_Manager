from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)



from ..database.handlers.database_handler import DataBaseHandler
from ..schemas.customer_schema import CustomerSchema
from ..schemas.database_filter import DBFilter
from ..services.parsers import IDParser
from ..validators.id_validator import IDValidator
from ..validators.db_validators import DBValidator
from ..models import Customer

@api_controller('/customer', tags=['Customer'])
class CustomerController:
    
    @route.get('', response=PaginatedResponseSchema[CustomerSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_customers(self, dbfilter: Query[DBFilter]):
        customers = DataBaseHandler.get_all(Customer, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(customers)
        return customers
    
    @route.get('/{ids}', response=PaginatedResponseSchema[CustomerSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_customers_by_id(self, ids: str, dbfilter: Query[DBFilter]):
        
        IDValidator.is_valid_id_type(ids)
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        customers = DataBaseHandler.get_by_ids(Customer, parsed_ids, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(customers)
        return customers
    