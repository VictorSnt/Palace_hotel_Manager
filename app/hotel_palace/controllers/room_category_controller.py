from ninja import Path
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)

from ..database.handlers.category_handler import CategoryHandler
from ..schemas.room_category_schemas import RoomCategoryResponseSchema
from ..validators.db_validators import DBValidator
from ..validators.id_validator import IDValidator
from ..services.parsers import IDParser

@api_controller('/category', tags=['Category'])
class RoomCategoryController:
    
    @route.get('', 
        response=PaginatedResponseSchema[RoomCategoryResponseSchema]
    )
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_rooms(self):
        categorys = CategoryHandler.get_all_categories()
        DBValidator.is_valid_and_not_empty_queryset(categorys)
        return categorys
    
    @route.get('/{ids}', 
        response=PaginatedResponseSchema[RoomCategoryResponseSchema]
    )
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_rooms_by_id(self, ids: str = Path(
        ..., description="Lista de IDs separados por vírgula"
        )):
        
        IDValidator.is_valid_id_type(ids)
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        categorys = CategoryHandler.get_categories_by_ids(parsed_ids)
        DBValidator.is_valid_and_not_empty_queryset(categorys)
        return categorys