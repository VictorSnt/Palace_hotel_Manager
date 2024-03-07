from django.db.models.query import QuerySet
from ..validators.exceptions import DBValidationError
from ..services.errors.error_payload_generator import ErrorPayloadGenerator


class DBValidator:
    
    @staticmethod
    def is_valid_and_not_empty_queryset(queryset: QuerySet):
        if not queryset.exists():
            ErrorPayloadGenerator.generate_error_payload(
                exc=DBValidationError,
                status_code=404,
                type='NotFoundOnDbError',
                title='Empty queryset',
                detail='No data returned from your query'
            )
                
                
                
            
            
            