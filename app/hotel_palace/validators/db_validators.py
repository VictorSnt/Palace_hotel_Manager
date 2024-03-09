from django.db.models.query import QuerySet
from django.db.models import Model
from django.forms.models import model_to_dict
from ninja import Schema
from ..services.errors.exceptions import DBValidationError
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
    def is_created_or_already_exist(is_created: bool, obj: Model) -> None:  
        
        if not is_created:
            unique_fields = [
                field.name for field in obj._meta.fields 
                if field.unique]
            obj_dict = model_to_dict(obj, unique_fields)
            invalid_params = [
                {
                    'obj_unique_fields': obj_dict,
                    'reason': 'you cant use the( keys, values) above'
                }
            ]
            ErrorPayloadGenerator.generate_error_payload(
                exc=DBValidationError,
                status_code=409,
                type='ObjectAlreadyExist',
                title='Unique field conflict',
                detail='There is a object with the '
                'same values in database',
                invalid_params=invalid_params
            )
           
                
            