from uuid import UUID
from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)
from ..schemas.generic import IdList

from ..schemas.models.reservation_schema import (
    CreateReservationSchema, ReservationOutSchema, UpdateReservationSchema
)
from ..schemas.query_strings.database_filter import DBFilter
from ..schemas.reponses.success_schemas import SuccessDetailed
from ..schemas.reponses.error_schemas import ErrorDetailed
from ..services.controller_services.reservation_service import (
    ReservationService
)
from ..models import Reservation


@api_controller('/reservation', tags=['Reservation'])
class ReservationController:
    
    paginated_reservs = {
        200: PaginatedResponseSchema[ReservationOutSchema],
    }
    reserv = {
        200: ReservationOutSchema,
    }
    post_method_responses = {
        201: SuccessDetailed,
        409: ErrorDetailed,
        422: ErrorDetailed
    }
    
    @route.get('/list', response=paginated_reservs)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_by_ids(self, id_list: Query[IdList], dbfilter: Query[DBFilter]):
        return ReservationService.get_by_ids(Reservation, id_list.ids, dbfilter)
    
    @route.put('/{id}')
    def update(self, id, updater_schema: UpdateReservationSchema):
        return ReservationService.update(Reservation, id, updater_schema)
    
    @route.get('/{id}', response=reserv)
    def get_reservations_by_id(self, id: UUID):
        return ReservationService.get_by_id(Reservation, id)
    
    @route.delete('/{id}')
    def delete(self, id):
        return ReservationService.delete(Reservation, id)

    @route.post('', response=post_method_responses)
    def create(self, reservation: CreateReservationSchema):
        return ReservationService.create(Reservation, reservation)
    
    @route.get('', response=paginated_reservs)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_reservations(self, dbfilter: Query[DBFilter]):
        return ReservationService.get_all(Reservation, dbfilter)
        