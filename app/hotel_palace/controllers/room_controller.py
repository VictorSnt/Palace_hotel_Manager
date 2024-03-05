from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)

from ..services.room_service import RoomService
from ..schemas.room_schemas import RoomResponseSchema
from ..schemas.database_filter import DBFilter

@api_controller('/room', tags=['Room'])
class RoomController:
    
    @route.get('', response=PaginatedResponseSchema[RoomResponseSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_rooms(self, dbfilter: Query[DBFilter]):
        rooms = RoomService.get_all_rooms(dbfilter)
        return rooms
    
    @route.get('/{ids}', response=PaginatedResponseSchema[RoomResponseSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_rooms_by_id(self, ids: str, dbfilter: Query[DBFilter]):
        rooms = RoomService.get_rooms_by_ids(ids, dbfilter)
        return rooms
    