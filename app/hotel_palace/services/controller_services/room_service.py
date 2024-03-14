from typing import Any, List
from django.db.models import Model
from ninja import Schema
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
    def get_all(dbfilter: DBFilter) -> RoomList:
        RoomService._validate_db_field(dbfilter)
        rooms = DataBaseHandler.get_all(Room, dbfilter)
        RoomService._validate_queryset(rooms)
        return rooms
    
    @staticmethod
    def get_by_ids(ids: str, dbfilter: DBFilter) -> RoomList:
        RoomService._validate_db_field(dbfilter) 
        ids = RoomService._validate_uuid(ids)
        rooms = DataBaseHandler.get_by_ids(Room, ids, dbfilter)
        RoomService._validate_queryset(rooms)
        return rooms
    
    @staticmethod
    def create(room: RoomInSchema) -> Success201:
        RoomService._validate_enum(room.status, 'status')
        id = RoomService._validate_uuid(room.category)
        category = DataBaseHandler.get_by_ids(Category, id)
        RoomService._validate_queryset(category)
        parsed_category = RoomService._parse_schema(room, category)
        args = Room, parsed_category
        response = DataBaseHandler.try_to_create(*args)
        RoomService._validate_obj_creation(response)
        return 201, {'message': 'Criado com sucesso'}
    
    @staticmethod
    def _validate_db_field(dbfilter: DBFilter) -> None:
        DBValidator.is_valid_db_field(Room, dbfilter.order_by)

    @staticmethod
    def _validate_queryset(rooms: RoomList) -> None:
        DBValidator.is_valid_and_not_empty_queryset(rooms)
        
    @staticmethod
    def _validate_uuid(ids: str) -> str :
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        return parsed_ids
    
    @staticmethod
    def _validate_enum(attr: str, attr_name: str):
        EnumValidator.validate_enum(RoomStatus, attr, attr_name)
        
    @staticmethod    
    def _parse_schema(schema: Schema, *args) -> dict[str, Any]:
        schema_dict = schema.model_dump()
        for arg in args:
            arg = arg.first()
            arg_name = str(arg.__class__.__name__).lower()
            schema_dict[arg_name] = arg
        return schema_dict
    
    @staticmethod
    def _validate_obj_creation(response: tuple[bool, Model]) -> None:
        room_obj, is_created = response
        DBValidator.is_created_or_already_exist(is_created, room_obj)
    