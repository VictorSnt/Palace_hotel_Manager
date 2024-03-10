from django.http import HttpResponse
from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)
from ..schemas.models.product_schema import (
    ProductInSchema, ProductOutSchema
)
from ..schemas.query_strings.database_filter import DBFilter
from ..services.controller_services.product_service import ProductService

@api_controller('/products', tags=['Products'])
class ProductController:
    
    @route.get('', response=PaginatedResponseSchema[ProductOutSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_products(self, dbfilter: Query[DBFilter]):
        return ProductService.get_all_products(dbfilter)
    
    @route.get('/{ids}', response=PaginatedResponseSchema[ProductOutSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_products_by_id(self, ids: str, dbfilter: Query[DBFilter]):
        return ProductService.get_products_by_ids(ids, dbfilter)

    @route.post('')
    def create_product(self, product: ProductInSchema):
        status_code = ProductService.create_product(product)
        return HttpResponse(status=status_code)