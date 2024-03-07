from typing import List
from ...database.handlers.database_handler import DataBaseHandler
from ...models import Category
from ...schemas.category_schemas import CategoryResponseSchema
from ...schemas.database_filter import DBFilter
from ...validators.id_validator import IDValidator
from ...validators.db_validators import DBValidator
from ...services.trasformators.parsers import IDParser


class CategoryService:
    
    @staticmethod
    def get_all_categories(dbfilter: DBFilter) -> List[CategoryResponseSchema]:
        categories = DataBaseHandler.get_all(Category, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(categories)
        return categories
    
    @staticmethod
    def get_categories_by_ids(ids: str, dbfilter: DBFilter) -> List[CategoryResponseSchema]:
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        categories = DataBaseHandler.get_by_ids(Category, parsed_ids, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(categories)
        return categories
