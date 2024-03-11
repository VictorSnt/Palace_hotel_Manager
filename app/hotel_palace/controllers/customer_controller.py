from django.http import HttpResponse
from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)
from ..schemas.models.customer_schema import (
    CustomerInSchema, CustomerOutSchema
)
from ..schemas.query_strings.database_filter import DBFilter
from ..services.controller_services.customer_service import CustomerService

@api_controller('/customer', tags=['Customer'])
class CustomerController:
    
    @route.get('', response=PaginatedResponseSchema[CustomerOutSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_customers(self, dbfilter: Query[DBFilter]):
        return CustomerService.get_all_customers(dbfilter)
    
    @route.get('/{ids}', response=PaginatedResponseSchema[CustomerOutSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_customers_by_id(self, ids: str, dbfilter: Query[DBFilter]):
        return CustomerService.get_customers_by_ids(ids, dbfilter)

    @route.post('')
    def create_customer(self, customer: CustomerInSchema):
        status_code = CustomerService.create_customer(customer)
        return HttpResponse(status=status_code)