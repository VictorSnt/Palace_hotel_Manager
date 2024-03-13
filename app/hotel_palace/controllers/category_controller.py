from django.http import HttpResponse
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)
from ninja_extra import api_controller, route
from ninja import Query
from ..services.controller_services.room_category_service import CategoryService
from ..schemas.models.category_schemas import (
    CategoryInSchema, CategoryOutSchema
)
from ..schemas.query_strings.database_filter import DBFilter
from ..schemas.reponses.error_schemas import ErrorDetailed
from ..schemas.reponses.success_schemas import SuccessDetailed

@api_controller('/category', tags=['Category'])
class CategoryController:
    
    get_method_responses = {
        200: PaginatedResponseSchema[CategoryOutSchema],
        404: ErrorDetailed,
        422: ErrorDetailed
    }
    post_method_responses = {
        201: SuccessDetailed,
        409: ErrorDetailed,
        422: ErrorDetailed
    }
    
    
    @route.get('', response=get_method_responses)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_categories(self, dbfilter: Query[DBFilter]):
        categories = CategoryService.get_all_categories(dbfilter)
        return categories
    
    @route.get('/{ids}', response=get_method_responses)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_categories_by_id(self, ids: str, dbfilter: Query[DBFilter]):
        categories = CategoryService.get_categories_by_ids(ids, dbfilter)
        return categories

    @route.post('/', response=post_method_responses)
    def create_category(self, category: CategoryInSchema):
        CategoryService.create_category(category)
        return 201, {'message': 'Criado com sucesso'}
