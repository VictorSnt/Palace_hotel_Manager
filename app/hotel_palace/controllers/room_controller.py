from django.http import HttpResponse
from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)

from ..services.controller_services.room_service import RoomService
from ..schemas.models.room_schemas import RoomSchema, RoomCreationSchema
from ..schemas.query_strings.database_filter import DBFilter

@api_controller('/room', tags=['Room'])
class RoomController:
    
    @route.get('', response=PaginatedResponseSchema[RoomSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_rooms(self, dbfilter: Query[DBFilter]):
        rooms = RoomService.get_all_rooms(dbfilter)
        return rooms
    
    @route.get('/{ids}', response=PaginatedResponseSchema[RoomSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_rooms_by_id(self, ids: str, dbfilter: Query[DBFilter]):
        rooms = RoomService.get_rooms_by_ids(ids, dbfilter)
        return rooms
    
    @route.post('')
    def create_room(self, room: RoomCreationSchema):
        status_code = RoomService.create_room(room=room)
        return HttpResponse(status=status_code)
        