from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)

from ..services.controller_services.room_category_service import CategoryService
from ..schemas.models.category_schemas import CategoryResponseSchema
from ..schemas.query_strings.database_filter import DBFilter

@api_controller('/category', tags=['Category'])
class CategoryController:
    
    @route.get('', 
        response=PaginatedResponseSchema[CategoryResponseSchema]
    )
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_rooms(self, dbfilter: Query[DBFilter]):
        categories = CategoryService.get_all_categories(dbfilter)
        return categories
    
    @route.get('/{ids}', 
        response=PaginatedResponseSchema[CategoryResponseSchema]
    )
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_rooms_by_id(self, ids: str, dbfilter: Query[DBFilter]):
        categories = CategoryService.get_categories_by_ids(ids, dbfilter)
        return categories
