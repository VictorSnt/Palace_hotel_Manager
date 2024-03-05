from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)

from ..database.handlers.database_handler import DataBaseHandler
from ..schemas.room_schemas import RoomResponseSchema
from ..schemas.database_filter import DBFilter
from ..validators.id_validator import IDValidator
from ..validators.db_validators import DBValidator
from ..services.parsers import IDParser
from ..models import Room


@api_controller('/room', tags=['Room'])
class RoomController:
    
    @route.get('', response=PaginatedResponseSchema[RoomResponseSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_rooms(self, dbfilter: Query[DBFilter]):
        rooms = DataBaseHandler.get_all(Room, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(rooms)
        return rooms
    
    @route.get('/{ids}', response=PaginatedResponseSchema[RoomResponseSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_rooms_by_id(self, ids: str, dbfilter: Query[DBFilter]):
        """
        Args:
            ids (str): [Lista de IDs separados por vírgula.]
        """
        IDValidator.is_valid_id_type(ids)
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        rooms = DataBaseHandler.get_by_ids(Room, parsed_ids, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(rooms)
        return rooms
    
