from typing import List, Tuple
from ...database.handlers.database_handler import DataBaseHandler
from ...models import Room, Category
from ...schemas.models.room_schemas import RoomInSchema, RoomOutSchema
from ...schemas.query_strings.database_filter import DBFilter
from ...schemas.reponses.success_schemas import SuccessDetailed
from ...services.base_service import BaseService
from ...utils.enums.room_status import RoomStatus


class RoomService(BaseService):
    # todo: Create a types module
    RoomList = List[RoomOutSchema]
    Success201  = Tuple[int, SuccessDetailed]
    
    @staticmethod
    def get_all(dbfilter: DBFilter) -> RoomList:
        RoomService._validate_db_field(Room, dbfilter)
        rooms = DataBaseHandler.get_all(Room, dbfilter)
        RoomService._validate_queryset(rooms)
        return rooms
    
    @staticmethod
    def get_by_ids(ids: str, dbfilter: DBFilter) -> RoomList:
        RoomService._validate_db_field(Room, dbfilter) 
        ids = RoomService._validate_n_parse_uuid(ids)
        rooms = DataBaseHandler.get_by_ids(Room, ids, dbfilter)
        RoomService._validate_queryset(rooms)
        return rooms
    
    @staticmethod
    def create(room: RoomInSchema) -> Success201:
        RoomService._validate_enum(RoomStatus, room.status, 'status')
        id = RoomService._validate_n_parse_uuid(room.category)
        category = DataBaseHandler.get_by_ids(Category, id)
        RoomService._validate_queryset(category)
        parsed_room = RoomService._parse_schema(room, category)
        args = Room, parsed_room
        response = DataBaseHandler.try_to_create(*args)
        RoomService._validate_obj_creation(response)
        return 201, {'message': 'Criado com sucesso'}
    