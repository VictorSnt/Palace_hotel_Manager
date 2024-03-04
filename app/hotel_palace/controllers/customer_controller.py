from ninja import Path
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)

from ..database.handlers.customer_handler import CustomerHandler
from ..schemas.customer_schema import CustomerSchema
from ..services.parsers import IDParser
from ..validators.id_validator import IDValidator
from ..validators.db_validators import DBValidator


@api_controller('/customer', tags=['Customer'])
class CustomerController:
    
    @route.get('', response=PaginatedResponseSchema[CustomerSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_customers(self):
        customers = CustomerHandler.get_all_cutomers()
        DBValidator.is_valid_and_not_empty_queryset(customers)
        return customers
    
    @route.get('/{ids}', response=PaginatedResponseSchema[CustomerSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_customers_by_id(self, ids: str = Path(
        ..., description="Lista de IDs separados por vírgula"
        )):
        
        IDValidator.is_valid_id_type(ids)
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        customers = CustomerHandler.get_cutomers_by_ids(parsed_ids)
        DBValidator.is_valid_and_not_empty_queryset(customers)
        return customers
    
      