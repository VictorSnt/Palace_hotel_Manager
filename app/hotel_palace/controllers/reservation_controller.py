from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)
from ..schemas.models.reservation_schema import ReservationSchema
from ..schemas.query_strings.database_filter import DBFilter
from ..services.controller_services.reservation_service import ReservationService

@api_controller('/reservation', tags=['Reservation'])
class ReservationController:
    
    @route.get('', response=PaginatedResponseSchema[ReservationSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_products(self, dbfilter: Query[DBFilter]):
        return ReservationService.get_all_reservations(dbfilter)
    
    @route.get('/{ids}', response=PaginatedResponseSchema[ReservationSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_products_by_id(self, ids: str, dbfilter: Query[DBFilter]):
        return ReservationService.get_reservations_by_ids(ids, dbfilter)
