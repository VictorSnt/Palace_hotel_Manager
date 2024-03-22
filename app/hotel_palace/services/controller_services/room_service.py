from typing import List, Tuple
from ...database.handlers.database_handler import DataBaseHandler
from ...models import Room, Category
from ...schemas.models.room_schemas import (
    RoomInSchema, RoomOutSchema, RoomUpdaterSchema
)
from ...schemas.query_strings.database_filter import DBFilter
from ...schemas.reponses.success_schemas import SuccessDetailed
from ...services.base_service import BaseService
from ...utils.enums.room_status import RoomStatus


class RoomService(BaseService):
    # todo: Create a types module
    RoomList = List[RoomOutSchema]
    Success201  = Tuple[int, SuccessDetailed]
    
    @staticmethod
    def create(room: RoomInSchema) -> Success201:
        RoomService._validate_enum(RoomStatus, room.status, 'status')
        category = RoomService.get_by_ids(room.category, Category)
        parsed_room = RoomService._parse_schema(room, category)
        args = Room, parsed_room
        response = DataBaseHandler.try_to_create(*args)
        RoomService._validate_obj_creation(response)
        return 201, {'message': 'Criado com sucesso'}
    
    @staticmethod
    def update(id, update_schema: RoomUpdaterSchema):
        category = update_schema.category
        room = DataBaseHandler.get_by_ids(Room, id)
        if category:
            category = RoomService.get_by_ids(category, Category)
        update_schema = RoomService._parse_schema(update_schema, category)
        DataBaseHandler.update(room.first(), update_schema)
        return 200, {'message': 'Atualizado com sucesso'}
    