from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)

from ..models import Accommodation
from ..schemas.query_strings.database_filter import DBFilter
from ..schemas.models.accomodation_schema import (
    AccommodationInSchema, AccommodationOutSchema
)
from ..services.controller_services.accommodation_service import (
    AccommodationService
)
from ..schemas.reponses.error_schemas import ErrorDetailed
from ..schemas.reponses.success_schemas import SuccessDetailed

@api_controller('/accommodation', tags=['Accommodations'])
class AccommodationController:
    
    get_method_responses = {
        200: PaginatedResponseSchema[AccommodationOutSchema],
        404: ErrorDetailed,
        422: ErrorDetailed
    }
    post_method_responses = {
        201: SuccessDetailed,
        409: ErrorDetailed,
        422: ErrorDetailed
    }
    
    @route.get('/{id}', response=get_method_responses)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_by_id(self, id: str, dbfilter: Query[DBFilter]):
        return AccommodationService.get_by_ids(id, Accommodation, dbfilter)
    
    @route.get('', response=get_method_responses)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get(self, dbfilter: Query[DBFilter]):
        return AccommodationService.get_all(Accommodation, dbfilter)
    
    @route.post('', response=post_method_responses)
    def create(self, accommodation: AccommodationInSchema):
        return AccommodationService.create(accommodation)
