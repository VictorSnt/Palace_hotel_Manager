from django.http import HttpResponse
from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)

from ..models import Reservation
from ..schemas.models.reservation_schema import (
    CreateReservationSchema, ReservationOutSchema
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
    
    
    @route.get('/{id}', response=get_method_responses)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_reservations_by_id(self, id: str, dbfilter: Query[DBFilter]):
        return ReservationService.get_by_ids(id, Reservation, dbfilter)
    
    @route.get('', response=get_method_responses)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_reservations(self, dbfilter: Query[DBFilter]):
        return ReservationService.get_all(Reservation, dbfilter)
    
    @route.post('', response=post_method_responses)
    def create(self, reservation: CreateReservationSchema):
        return ReservationService.create(Reservation, reservation)
        