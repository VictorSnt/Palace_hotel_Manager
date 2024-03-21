from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)
from ..schemas.models.room_schemas import RoomOutSchema, RoomInSchema
from ..services.controller_services.room_service import RoomService
from ..schemas.reponses.error_schemas import ErrorDetailed
from ..schemas.reponses.success_schemas import SuccessDetailed
from ..schemas.query_strings.database_filter import DBFilter


@api_controller('/room', tags=['Room'])
class RoomController:
    
    get_method_responses = {
        200: PaginatedResponseSchema[RoomOutSchema],
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
    def get(self, dbfilter: Query[DBFilter]):
        return RoomService.get_all(dbfilter)
         
    @route.get('/{ids}', response=get_method_responses)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_by_id(self, ids: str, dbfilter: Query[DBFilter]):
        return RoomService.get_by_ids(ids, dbfilter)
         
    @route.post('', response=post_method_responses)
    def create(self, room: RoomInSchema):
        return RoomService.create(room=room)
    
    
         