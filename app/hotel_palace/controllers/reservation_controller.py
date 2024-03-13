from django.http import HttpResponse
from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)
from ..schemas.models.reservation_schema import (
    ReservationInSchema, ReservationOutSchema
)
from ..schemas.query_strings.database_filter import DBFilter
from ..services.controller_services.reservation_service import ReservationService
from ..schemas.reponses.success_schemas import SuccessDetailed
from ..schemas.reponses.error_schemas import ErrorDetailed

@api_controller('/reservation', tags=['Reservation'])
class ReservationController:
    
    get_method_responses = {
        200: PaginatedResponseSchema[ReservationOutSchema],
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
    def get_reservations(self, dbfilter: Query[DBFilter]):
        return ReservationService.get_all_reservations(dbfilter)
    
    @route.get('/{ids}', response=get_method_responses)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_reservations_by_id(self, ids: str, dbfilter: Query[DBFilter]):
        return ReservationService.get_reservations_by_ids(ids, dbfilter)

    @route.post('', response=post_method_responses)
    def create_reservation(self, reservation: ReservationInSchema):
        status_code = ReservationService.create_reservation(reservation)
        return HttpResponse(status=status_code)
