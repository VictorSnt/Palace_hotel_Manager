from typing import List
from ...database.handlers.database_handler import DataBaseHandler
from ...models import Room
from ...schemas.models.room_schemas import RoomSchema
from ...schemas.query_strings.database_filter import DBFilter
from ...validators.id_validator import IDValidator
from ...validators.db_validators import DBValidator
from ...services.trasformators.parsers import IDParser

class RoomService:
    
    @staticmethod
    def get_all_rooms(dbfilter: DBFilter) -> List[RoomSchema]:
        rooms = DataBaseHandler.get_all(Room, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(rooms)
        return rooms
    
    @staticmethod
    def get_rooms_by_ids(ids: str, dbfilter: DBFilter) -> List[RoomSchema]:
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        rooms = DataBaseHandler.get_by_ids(Room, parsed_ids, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(rooms)
        return rooms
