from typing import List
from ...schemas.reponses.success_schemas import SuccessDetailed
from ...database.handlers.database_handler import DataBaseHandler
from ...models import Category
from ...schemas.models.category_schemas import (
    CategoryInSchema, CategoryOutSchema
)
from ...schemas.query_strings.database_filter import DBFilter
from ...services.base_service import BaseService

class CategoryService(BaseService):
    
    CategoryList = List[CategoryOutSchema]
    Success201  = tuple[int, SuccessDetailed]
    
    @staticmethod
    def get_all(dbfilter: DBFilter) -> CategoryList:
        CategoryService._validate_db_field(Category, dbfilter) 
        categories = DataBaseHandler.get_all(Category, dbfilter)
        CategoryService._validate_queryset(categories)
        return categories
    
    @staticmethod
    def get_by_ids(ids: str, dbfilter: DBFilter) -> CategoryList:
        CategoryService._validate_db_field(Category, dbfilter) 
        ids = CategoryService._validate_n_parse_uuid(ids)
        categories = DataBaseHandler.get_by_ids(Category, ids, dbfilter)
        CategoryService._validate_queryset(categories)
        return categories

    @staticmethod
    def create(category: CategoryInSchema) -> Success201:
        args = Category, category.model_dump()
        response = DataBaseHandler.try_to_create(*args)
        CategoryService._validate_obj_creation(response)
        return 201, {'message': 'Criado com sucesso'}
