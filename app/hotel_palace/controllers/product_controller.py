from django.http import HttpResponse
from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)

from ..models import Product
from ..schemas.models.product_schema import (
    ProductInSchema, ProductOutSchema
)
from ..schemas.query_strings.database_filter import DBFilter
from ..services.controller_services.product_service import ProductService
from ..schemas.reponses.success_schemas import SuccessDetailed
from ..schemas.reponses.error_schemas import ErrorDetailed



@api_controller('/product', tags=['Products'])
class ProductController:
    
    get_method_responses = {
        200: PaginatedResponseSchema[ProductOutSchema],
        404: ErrorDetailed,
        422: ErrorDetailed
    }
    post_method_responses = {
        201: SuccessDetailed,
        409: ErrorDetailed,
        422: ErrorDetailed
    }
    
    @route.get('/{id}', response=get_method_responses)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_by_id(self, id: str, dbfilter: Query[DBFilter]):
        return ProductService.get_by_ids(id, Product, dbfilter)
    
    @route.get('', response=get_method_responses)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get(self, dbfilter: Query[DBFilter]):
        return ProductService.get_all(Product, dbfilter)

    @route.post('', response=post_method_responses)
    def create(self, product: ProductInSchema):
        return ProductService.create(product)
    