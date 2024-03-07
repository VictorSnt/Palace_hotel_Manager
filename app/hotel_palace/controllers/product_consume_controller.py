from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)
from ..schemas.product_consume_schema import ProductConsumeSchema
from ..schemas.database_filter import DBFilter
from ..services.product_consume_service import ProductConsumeService

@api_controller('/consume', tags=['Consumes'])
class ProductConsumeController:
    
    @route.get('', response=PaginatedResponseSchema[ProductConsumeSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_products(self, dbfilter: Query[DBFilter]):
        return ProductConsumeService.get_all_consumes(dbfilter)
    
    @route.get('/{ids}', response=PaginatedResponseSchema[ProductConsumeSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_products_by_id(self, ids: str, dbfilter: Query[DBFilter]):
        return ProductConsumeService.get_consumes_by_ids(ids, dbfilter)
