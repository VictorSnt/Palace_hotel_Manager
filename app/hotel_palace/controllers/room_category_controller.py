from ninja import Path, Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)

from ..database.handlers.database_handler import DataBaseHandler
from ..schemas.room_category_schemas import RoomCategoryResponseSchema
from ..schemas.database_filter import DBFilter
from ..validators.db_validators import DBValidator
from ..validators.id_validator import IDValidator
from ..services.parsers import IDParser
from ..models import RoomCategory

@api_controller('/category', tags=['Category'])
class RoomCategoryController:
    
    @route.get('', 
        response=PaginatedResponseSchema[RoomCategoryResponseSchema]
    )
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_rooms(self, dbfilter: Query[DBFilter]):
        categorys = DataBaseHandler.get_all(RoomCategory, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(categorys)
        return categorys
    
    @route.get('/{ids}', 
        response=PaginatedResponseSchema[RoomCategoryResponseSchema]
    )
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_rooms_by_id(self, ids: str, dbfilter: Query[DBFilter]):
        
        IDValidator.is_valid_id_type(ids)
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        categorys = DataBaseHandler.get_by_ids(
            RoomCategory, parsed_ids, dbfilter
        )
        DBValidator.is_valid_and_not_empty_queryset(categorys)
        return categorys
    