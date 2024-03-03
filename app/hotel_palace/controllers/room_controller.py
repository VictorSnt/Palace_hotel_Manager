from ..schemas.room_schemas import RoomResponseSchema
from ..models import Room
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)
from ninja_extra import api_controller, route
from django.http import HttpRequest
from typing import List

@api_controller('/room', tags=['Room'])
class RoomController:
    
    
    @route.get('', response=PaginatedResponseSchema[RoomResponseSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_rooms(self):
        return Room.objects.all()
    
    @route.get('{id}', response=PaginatedResponseSchema[RoomResponseSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_rooms_by_id(self, id):
        return Room.objects.filter(pk=id)
    