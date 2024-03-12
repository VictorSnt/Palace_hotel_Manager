from typing import List
from ...database.handlers.database_handler import DataBaseHandler
from ...models import Category
from ...schemas.models.category_schemas import (
    CategoryInSchema, CategoryOutSchema
)
from ...schemas.query_strings.database_filter import DBFilter
from ...validators.id_validator import IDValidator
from ...validators.db_validators import DBValidator
from ...services.trasformators.parsers import IDParser


class CategoryService:
    
    @staticmethod
    def get_all_categories(dbfilter: DBFilter) -> List[CategoryOutSchema]:
        DBValidator.is_valid_db_field(Category, dbfilter.order_by)  
        categories = DataBaseHandler.get_all(Category, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(categories)
        return categories
    
    @staticmethod
    def get_categories_by_ids(ids: str, dbfilter: DBFilter) -> List[CategoryOutSchema]:
        DBValidator.is_valid_db_field(Category, dbfilter.order_by)  
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        categories = DataBaseHandler.get_by_ids(Category, parsed_ids, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(categories)
        return categories

    @staticmethod
    def create_category(category: CategoryInSchema) -> int:
        category_obj, is_created = DataBaseHandler.try_to_create(
            Category, category.model_dump()
        )
        DBValidator.is_created_or_already_exist(is_created, category_obj)
        status_code = 201
        return status_code
    