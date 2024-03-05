from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)
from ..schemas.products_schema import ProductsSchema
from ..schemas.database_filter import DBFilter
from ..services.product_service import ProductService

@api_controller('/products', tags=['Products'])
class ProductController:
    
    @route.get('', response=PaginatedResponseSchema[ProductsSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_products(self, dbfilter: Query[DBFilter]):
        return ProductService.get_all_products(dbfilter)
    
    @route.get('/{ids}', response=PaginatedResponseSchema[ProductsSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_products_by_id(self, ids: str, dbfilter: Query[DBFilter]):
        return ProductService.get_products_by_ids(ids, dbfilter)
