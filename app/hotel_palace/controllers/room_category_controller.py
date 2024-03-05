from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)

from ..services.room_category_service import RoomCategoryService
from ..schemas.room_category_schemas import RoomCategoryResponseSchema
from ..schemas.database_filter import DBFilter

@api_controller('/category', tags=['Category'])
class RoomCategoryController:
    
    @route.get('', 
        response=PaginatedResponseSchema[RoomCategoryResponseSchema]
    )
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_rooms(self, dbfilter: Query[DBFilter]):
        categories = RoomCategoryService.get_all_categories(dbfilter)
        return categories
    
    @route.get('/{ids}', 
        response=PaginatedResponseSchema[RoomCategoryResponseSchema]
    )
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_rooms_by_id(self, ids: str, dbfilter: Query[DBFilter]):
        categories = RoomCategoryService.get_categories_by_ids(ids, dbfilter)
        return categories
