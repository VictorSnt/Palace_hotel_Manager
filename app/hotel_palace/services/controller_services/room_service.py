from ...database.handlers.database_handler import DataBaseHandler
from ...schemas.models.room_schemas import RoomUpdaterSchema
from ...services.base_service import BaseService
from ...models import Room, Category


class RoomService(BaseService):
    
    @staticmethod
    def update(id, update_schema: RoomUpdaterSchema):
        category = update_schema.category
        room = DataBaseHandler.get_by_ids(Room, id)
        if category:
            category = RoomService.get_by_ids(category, Category)
        update_schema = RoomService._parse_schema(update_schema, category)
        DataBaseHandler.update(room.first(), update_schema)
        return 200, {'message': 'Atualizado com sucesso'}
    