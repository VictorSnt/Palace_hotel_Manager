from django.http import HttpResponse
from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)
from ..schemas.models.consume_schema import (
    ConsumeInSchema, ConsumeOutSchema
)
from ..schemas.query_strings.database_filter import DBFilter
from ..services.controller_services.consume_service import ConsumeService


@api_controller('/consume', tags=['Consumes'])
class ConsumeController:
    
    @route.get('', response=PaginatedResponseSchema[ConsumeOutSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_products(self, dbfilter: Query[DBFilter]):
        return ConsumeService.get_all_consumes(dbfilter)
    
    @route.get('/{ids}', response=PaginatedResponseSchema[ConsumeOutSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_products_by_id(self, ids: str, dbfilter: Query[DBFilter]):
        return ConsumeService.get_consumes_by_ids(ids, dbfilter)
    
    @route.post('')
    def create_consume(self, consume: ConsumeInSchema):
        status_code = ConsumeService.create_consume(consume)
        return HttpResponse(status=status_code)
