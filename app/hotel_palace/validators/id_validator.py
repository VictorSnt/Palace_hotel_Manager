from uuid import UUID
from typing import Union, List
from ..services.errors.error_payload_generator import ErrorPayloadGenerator
from ..validators.exceptions import ValidationError


class IDValidator:
          
    @staticmethod
    def is_valid_uuid(ids: List[str]) -> None:
        invalid_uuids = []
        for id in ids:
            try:
                UUID(id)
            except ValueError:
                invalid_uuids.append(id)

        if invalid_uuids: 
            ErrorPayloadGenerator.generate_error_payload(
                exc=ValidationError,
                status_code=422,
                type='NotValidUUID',
                title='Must be UUID',
                detail='One of the arguments is invalid',
                invalid_params=[{
                    'name':'ids',
                    'values': ', '.join(invalid_uuids), 
                    'reason': 'the ids is not a valid UUID format',
                }] 
            )
