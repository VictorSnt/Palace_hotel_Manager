from uuid import UUID
from django.http import HttpResponse
from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)

from ..schemas.generic import IdList

from ..models import Consume
from ..schemas.models.consume_schema import (
    CreateConsumeSchema, ConsumeOutSchema
)
from ..schemas.query_strings.database_filter import DBFilter
from ..services.controller_services.consume_service import ConsumeService
from ..schemas.reponses.error_schemas import ErrorDetailed
from ..schemas.reponses.success_schemas import SuccessDetailed

@api_controller('/consume', tags=['Consumes'])
class ConsumeController:
    
    paginated_consumes = {
        200: PaginatedResponseSchema[ConsumeOutSchema],
        
    }
    consume = {
        200: ConsumeOutSchema,
        
    }
    post_method_responses = {
        201: SuccessDetailed,
        409: ErrorDetailed
    }
    
    @route.get('/list', response=paginated_consumes)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_by_ids(self, id_list: Query[IdList], dbfilter: Query[DBFilter]):
        return ConsumeService.get_by_ids(Consume, id_list.ids, dbfilter)
    
    @route.get('/{id}', response=consume)
    def get_by_id(self, id: UUID):
        return ConsumeService.get_by_id(Consume, id)
    
    @route.delete('/{id}')
    def delete(self, id):
        return ConsumeService.delete(Consume, id)

    @route.get('', response=paginated_consumes)
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get(self, dbfilter: Query[DBFilter]):
        return ConsumeService.get_all(Consume, dbfilter)
    
    @route.post('', response=post_method_responses)
    def create(self, consume: CreateConsumeSchema):
        return ConsumeService.create(Consume, consume)
    