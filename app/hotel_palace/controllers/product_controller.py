from uuid import UUID
from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)

from ..models import Product
from ..schemas.models.product_schema import (
    CreateProductSchema, ProductOutSchema, UpdateProductSchema
)
from ..schemas.query_strings.database_filter import DBFilter
from ..services.controller_services.product_service import ProductService
from ..schemas.reponses.success_schemas import SuccessDetailed
from ..schemas.reponses.error_schemas import ErrorDetailed
from ..schemas.generic import IdList


@api_controller('/product', tags=['Products'])
class ProductController:
    
    paginated_products = {
        200: PaginatedResponseSchema[ProductOutSchema],
    }
    product = {
        200: ProductOutSchema,
    }
    post_method_responses = {
        201: SuccessDetailed,
        409: ErrorDetailed,
        422: ErrorDetailed
    }
    
    @route.get('/list', response=paginated_products)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_by_ids(self, id_list: Query[IdList], dbfilter: Query[DBFilter]):
        return ProductService.get_by_ids(Product, id_list.ids, dbfilter)

    @route.put('/{id}')
    def update(self, id, updater_schema: UpdateProductSchema):
        return ProductService.update(Product, id, updater_schema)
    
    @route.get('/{id}', response=product)
    def get_by_id(self, id: UUID):
        return ProductService.get_by_id(Product, id)
    
    @route.get('', response=paginated_products)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get(self, dbfilter: Query[DBFilter]):
        return ProductService.get_all(Product, dbfilter)

    @route.post('', response=post_method_responses)
    def create(self, product: CreateProductSchema):
        return ProductService.create(Product, product)
    