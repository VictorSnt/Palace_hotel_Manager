from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)
from ..schemas.room_accomodation_schema import RoomAccommodationSchema
from ..schemas.database_filter import DBFilter
from ..services.accommodation_service import AccommodationService


PaginatedAccommodations = PaginatedResponseSchema[RoomAccommodationSchema]

@api_controller('/accommodation', tags=['Accommodations'])
class AccommodationController:
    
    @route.get('', response=PaginatedAccommodations)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_customers(self, dbfilter: Query[DBFilter]):
        return AccommodationService.get_all_accommodations(dbfilter)
    
    @route.get('/{ids}', response=PaginatedAccommodations)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_customers_by_id(self, ids: str, dbfilter: Query[DBFilter]):
        return AccommodationService.get_accommodations_by_ids(ids, dbfilter)
