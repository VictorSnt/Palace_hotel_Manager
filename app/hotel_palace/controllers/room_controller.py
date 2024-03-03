from django.http import HttpRequest

from ninja import Path
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)

from ..database.handlers.room_handler import RoomHandler
from ..models import Room
from ..schemas.room_schemas import RoomResponseSchema
from ..services.parsers import IDParser
from ..validators.id_validator import IDValidator
from ..validators.db_validators import DBValidator


@api_controller('/room', tags=['Room'])
class RoomController:
    
    @route.get('', response=PaginatedResponseSchema[RoomResponseSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_rooms(self):
        rooms = RoomHandler.get_all_rooms()
        DBValidator.is_valid_and_not_empty_queryset(rooms)
        return rooms
    
    @route.get('/{ids}', response=PaginatedResponseSchema[RoomResponseSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_rooms_by_id(self, ids: str = Path(
        ..., description="Lista de IDs separados por vírgula"
        )):
        
        IDValidator.is_valid_id_type(ids)
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        rooms = RoomHandler.get_rooms_by_ids(parsed_ids)
        DBValidator.is_valid_and_not_empty_queryset(rooms)
        return rooms
        