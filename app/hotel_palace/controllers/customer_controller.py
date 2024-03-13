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
from ..schemas.reponses.success_schemas import SuccessDetailed
from ..schemas.reponses.error_schemas import ErrorDetailed



@api_controller('/customer', tags=['Customer'])
class CustomerController:
    
    get_method_responses = {
        200: PaginatedResponseSchema[CustomerOutSchema],
        404: ErrorDetailed,
        422: ErrorDetailed
    }
    post_method_responses = {
        201: SuccessDetailed,
        409: ErrorDetailed,
        422: ErrorDetailed
    }
    
    
    @route.get('', response=get_method_responses)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_customers(self, dbfilter: Query[DBFilter]):
        return CustomerService.get_all_customers(dbfilter)
    
    @route.get('/{ids}', response=get_method_responses)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_customers_by_id(self, ids: str, dbfilter: Query[DBFilter]):
        return CustomerService.get_customers_by_ids(ids, dbfilter)

    @route.post('', response=post_method_responses)
    def create_customer(self, customer: CustomerInSchema):
        CustomerService.create_customer(customer)
        return 201, {'message': 'Criado com sucesso'}