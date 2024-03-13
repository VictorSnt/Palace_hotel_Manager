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
            invalid_params = [
                {
                    'name': 'ids',
                    'reason': 'No data found with this pk'
                }
            ]
            ErrorPayloadGenerator.generate_422_error_detailed(
                exc=DBValidationError,
                status_code=404,
                type='NotFoundOnDbError',
                title='Empty queryset',
                detail='No data returned from your query',
                invalid_params=invalid_params
            )
    
    def is_created_or_already_exist(is_created: bool, obj: Model) -> None:  
        
        if not is_created:
            unique_fields = [
                field.name for field in obj._meta.fields 
                if field.unique]
            obj_dict = model_to_dict(obj, unique_fields)
            invalid_params = [
                {
                    'name': obj.__class__.__name__,
                    'reason': f'you cant use the({obj_dict}) it must be unique'
                }
            ]
            ErrorPayloadGenerator.generate_422_error_detailed(
                exc=DBValidationError,
                status_code=409,
                type='ObjectAlreadyExist',
                title='Unique field conflict',
                detail='There is a object with the '
                'same values in database',
                invalid_params=invalid_params
            )
           
    def is_valid_db_field(model: Model, field: str):
        if not field:
            return
        existent_fields = [str(field.name) for field in model._meta.fields]
        if not field in existent_fields:
            invalid_params = {
                'name': field,
                'reason': f'the avaliable fields are: {existent_fields}'
            }
            ErrorPayloadGenerator.generate_422_error_detailed(
                exc=DBValidationError,
                status_code=422,
                type='FieldDoesNotExist',
                title=f'The field ({field}) dont exist',
                detail='You tried to order by a inexistent field',
                invalid_params=invalid_params
            )
                
            