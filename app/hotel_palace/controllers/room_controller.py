from uuid import UUID
from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)


from ..models import Room
from ..schemas.models.room_schemas import (
    RoomOutSchema, CreateRoomSchema, RoomUpdaterSchema
)
from ..services.controller_services.room_service import RoomService
from ..schemas.reponses.success_schemas import SuccessDetailed
from ..schemas.query_strings.database_filter import DBFilter
from ..schemas.generic import IdList


@api_controller('/room', tags=['Room'])
class RoomController:
    
    paginated_rooms = {
        200: PaginatedResponseSchema[RoomOutSchema],
    }
    rooms_response = {
        200: RoomOutSchema,
    }
    post_method_responses = {
        201: SuccessDetailed
    }
    
    @route.get('/list', response=paginated_rooms)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_by_ids(self, id_list: Query[IdList], dbfilter: Query[DBFilter]):
        return RoomService.get_by_ids(Room, id_list.ids, dbfilter)
    
    @route.put('/{id}')
    def update(self, id, updater_schema: RoomUpdaterSchema):
        return RoomService.update(Room, id, updater_schema)

    @route.get('/{id}', response=rooms_response)
    def get_by_id(self, id: UUID):
        return RoomService.get_by_id(Room, id)

    @route.post('', response=post_method_responses)
    def create(self, room: CreateRoomSchema):
        return RoomService.create(Room, room)

    @route.get('', response=paginated_rooms)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get(self, dbfilter: Query[DBFilter]):
        return RoomService.get_all(Room, dbfilter)

    

    
         