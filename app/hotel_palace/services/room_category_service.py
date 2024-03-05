from typing import List
from ..database.handlers.database_handler import DataBaseHandler
from ..models import RoomCategory
from ..schemas.room_category_schemas import RoomCategoryResponseSchema
from ..schemas.database_filter import DBFilter
from ..validators.id_validator import IDValidator
from ..validators.db_validators import DBValidator
from ..services.parsers import IDParser

class RoomCategoryService:
    
    @staticmethod
    def get_all_categories(dbfilter: DBFilter) -> List[RoomCategoryResponseSchema]:
        categories = DataBaseHandler.get_all(RoomCategory, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(categories)
        return categories
    
    @staticmethod
    def get_categories_by_ids(ids: str, dbfilter: DBFilter) -> List[RoomCategoryResponseSchema]:
        IDValidator.is_valid_id_type(ids)
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        categories = DataBaseHandler.get_by_ids(RoomCategory, parsed_ids, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(categories)
        return categories
