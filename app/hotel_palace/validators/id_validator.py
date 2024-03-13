from uuid import UUID
from typing import List
from ..services.errors.error_payload_generator import ErrorPayloadGenerator
from ..services.errors.exceptions import ValidationError


class IDValidator:
          
    @staticmethod
    def is_valid_uuid(ids: List[str], param_name='ids') -> None:
        invalid_uuids = []
        for id in ids:
            try:
                UUID(id)
            except ValueError:
                invalid_uuids.append(id)

        if invalid_uuids: 
            ErrorPayloadGenerator.generate_422_error_detailed(
                exc=ValidationError,
                status_code=422,
                type='NotValidUUID',
                title='Must be UUID',
                detail='One of the arguments is invalid',
                invalid_params=[{
                    'name': param_name,
                    'reason': f'the ids ({", ".join(invalid_uuids)}) '
                    'is not a valid UUID format',
                }] 
            )
