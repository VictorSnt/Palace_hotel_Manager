from django.http import HttpResponse
from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)

from ..models import Consume
from ..schemas.models.consume_schema import (
    ConsumeInSchema, ConsumeOutSchema
)
from ..schemas.query_strings.database_filter import DBFilter
from ..services.controller_services.consume_service import ConsumeService
from ..schemas.reponses.error_schemas import ErrorDetailed
from ..schemas.reponses.success_schemas import SuccessDetailed

@api_controller('/consume', tags=['Consumes'])
class ConsumeController:
    
    get_method_responses = {
        200: PaginatedResponseSchema[ConsumeOutSchema],
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
        return ConsumeService.get_by_ids(id, Consume, dbfilter)
    
    @route.get('', response=get_method_responses)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get(self, dbfilter: Query[DBFilter]):
        return ConsumeService.get_all(Consume, dbfilter)
    
    @route.post('', response=post_method_responses)
    def create(self, consume: ConsumeInSchema):
        return ConsumeService.create(consume)
        
