from uuid import UUID
from django.http import HttpResponse
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)
from ninja_extra import api_controller, route
from ninja import Query

from ..schemas.generic import IdList

from ..models import Category
from ..services.controller_services.category_service import CategoryService
from ..schemas.models.category_schemas import (
    CreateCategorySchema, CategoryOutSchema, UpdateCategorySchema
)
from ..schemas.query_strings.database_filter import DBFilter
from ..schemas.reponses.error_schemas import ErrorDetailed
from ..schemas.reponses.success_schemas import SuccessDetailed

@api_controller('/category', tags=['Category'])
class CategoryController:
    
    paginated_categories = {
        200: PaginatedResponseSchema[CategoryOutSchema],
    }
    category = {
        200: CategoryOutSchema
    }
    
    post_method_responses = {
        201: SuccessDetailed,
        409: ErrorDetailed,
        422: ErrorDetailed
    }
    
    @route.get('/list', response=paginated_categories)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_by_ids(self, id_list: Query[IdList], dbfilter: Query[DBFilter]):
        return CategoryService.get_by_ids(Category, id_list.ids, dbfilter)
    
    @route.put('/{id}')
    def update(self, id, updater_schema: UpdateCategorySchema):
        return CategoryService.update(Category, id, updater_schema)

    @route.get('/{id}', response=category)
    def get_by_id(self, id: UUID):
       return CategoryService.get_by_id(Category, id)
   
    @route.get('', response=paginated_categories)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get(self, dbfilter: Query[DBFilter]):
       return CategoryService.get_all(Category, dbfilter)

    @route.post('', response=post_method_responses)
    def create(self, category: CreateCategorySchema): 
        return CategoryService.create(Category, category)
