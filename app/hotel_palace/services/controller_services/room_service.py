from typing import List
from ...database.handlers.database_handler import DataBaseHandler
from ...models import Room, Category
from ...schemas.models.room_schemas import RoomInSchema, RoomOutSchema
from ...schemas.query_strings.database_filter import DBFilter
from ...schemas.reponses.success_schemas import SuccessDetailed
from ...validators.id_validator import IDValidator
from ...validators.db_validators import DBValidator
from ...validators.enum_validator import EnumValidator
from ...services.trasformators.parsers import IDParser
from ...utils.enums.room_status import RoomStatus


class RoomService:
    
    RoomList = List[RoomOutSchema]
    Success201  = tuple[int, SuccessDetailed]
    
    @staticmethod
    def get_all_rooms(dbfilter: DBFilter) -> RoomList:
        DBValidator.is_valid_db_field(Room, dbfilter.order_by)  
        rooms = DataBaseHandler.get_all(Room, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(rooms)
        return rooms
    
    @staticmethod
    def get_rooms_by_ids(ids: str, dbfilter: DBFilter) -> RoomList:
        DBValidator.is_valid_db_field(Room, dbfilter.order_by)  
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        rooms = DataBaseHandler.get_by_ids(Room, parsed_ids, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(rooms)
        return rooms
    
    @staticmethod
    def create_room(room: RoomInSchema) -> Success201:
        status = room.status
        category_id = room.category
        EnumValidator.validate_enum(RoomStatus, status, 'status')
        parsed_ids = IDParser.paser_ids_by_comma(category_id)
        IDValidator.is_valid_uuid(parsed_ids, param_name='category')
        category = DataBaseHandler.get_by_ids(Category, parsed_ids)
        DBValidator.is_valid_and_not_empty_queryset(category)
        room_dict = room.model_dump()
        room_dict['category'] = category.first()
        room_obj, is_created = DataBaseHandler.try_to_create(Room, room_dict)
        DBValidator.is_created_or_already_exist(is_created, room_obj)
        return 201, {'message': 'Criado com sucesso'}
    