from uuid import UUID
from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)

from ..schemas.generic import IdList

from ..models import Accommodation
from ..schemas.query_strings.database_filter import DBFilter
from ..schemas.models.accomodation_schema import (
    CreateAccommodationSchema, AccommodationOutSchema, UpdateAccommodationSchema
)
from ..services.controller_services.accommodation_service import (
    AccommodationService
)
from ..schemas.reponses.error_schemas import ErrorDetailed
from ..schemas.reponses.success_schemas import SuccessDetailed

@api_controller('/accommodation', tags=['Accommodations'])
class AccommodationController:
    
    paginated_accomm = {
        200: PaginatedResponseSchema[AccommodationOutSchema],
    }
    
    accomm = {
        200: AccommodationOutSchema
    }
    
    post_method_responses = {
        201: SuccessDetailed,
        409: ErrorDetailed,
        422: ErrorDetailed
    }
    
    @route.get('/list', response=paginated_accomm)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_by_ids(self, id_list: Query[IdList], dbfilter: Query[DBFilter]):
        args = Accommodation, id_list.ids, dbfilter
        return AccommodationService.get_by_ids(*args)
    
    @route.put('/{id}')
    def update(self, id, updater_schema: UpdateAccommodationSchema):
        return AccommodationService.update(Accommodation, id, updater_schema)
    
    @route.delete('/{id}')
    def delete(self, id):
        return AccommodationService.delete(Accommodation, id)

    @route.get('/{id}', response=accomm)
    def get_by_id(self, id: UUID):
        return AccommodationService.get_by_id(Accommodation, id)
    
    @route.post('', response=post_method_responses)
    def create(self, accommodation: CreateAccommodationSchema):
        return AccommodationService.create(Accommodation, accommodation)
    
    @route.get('', response=paginated_accomm)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get(self, dbfilter: Query[DBFilter]):
        return AccommodationService.get_all(Accommodation, dbfilter)
    