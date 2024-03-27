from uuid import UUID
from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)

from ..schemas.models.accomodation_schema import AccommodationOutSchema

from ..schemas.generic import IdList

from ..models import Customer
from ..schemas.models.customer_schema import (
    CreateOrUpdateCustomerSchema, CustomerOutSchema
)
from ..schemas.query_strings.database_filter import DBFilter
from ..services.controller_services.customer_service import CustomerService
from ..schemas.reponses.success_schemas import SuccessDetailed
from ..schemas.reponses.error_schemas import ErrorDetailed



@api_controller('/customer', tags=['Customer'])
class CustomerController:
    
    paginated_customer = {
        200: PaginatedResponseSchema[CustomerOutSchema],
    }
    paginated_accomm = {
        200: PaginatedResponseSchema[AccommodationOutSchema],
    }
    customer = {
        200: CustomerOutSchema,
    }
    post_method_responses = {
        201: SuccessDetailed,
        409: ErrorDetailed,
        422: ErrorDetailed
    }
    
    @route.get('/list', response=paginated_customer)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_by_ids(self, id_list: Query[IdList], dbfilter: Query[DBFilter]):
        return CustomerService.get_by_ids(Customer, id_list.ids, dbfilter)

    @route.get('/accommodations', response=paginated_accomm)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_accommodations(self, id):
        key = "accommodations"
        return CustomerService.get_obj_backref(Customer, id, key)
    
    @route.put('/{id}')
    def update(self, id, updater_schema: CreateOrUpdateCustomerSchema):
        return CustomerService.update(Customer, id, updater_schema)
    
    @route.delete('/{id}')
    def delete(self, id):
        return CustomerService.delete(Customer, id)
    
    @route.get('/{id}', response=customer)
    def get_by_id(self, id: UUID):
        return CustomerService.get_by_id(Customer, id)
    
    @route.get('', response=paginated_customer)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get(self, dbfilter: Query[DBFilter]):
        return CustomerService.get_all(Customer, dbfilter)

    @route.post('', response=post_method_responses)
    def create_customer(self, customer: CreateOrUpdateCustomerSchema):
        return CustomerService.create(Customer, customer)
    