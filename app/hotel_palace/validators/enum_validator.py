from enum import Enum
from typing import List
from ..services.errors.error_payload_generator import ErrorPayloadGenerator
from ..services.errors.exceptions import ValidationError


class EnumValidator:
    
    @staticmethod
    def validate_enum(enum: Enum, value: str, param_name: str):
        if not value in [e.name for e in enum]:
            ErrorPayloadGenerator.generate_422_error_detailed(
                exc=ValidationError,
                status_code=422,
                type='NotValidParam',
                title='One or more the arguments is invalid',
                detail=f'{param_name} must be valid, {value} is invalid',
                invalid_params=[{
                    'name': param_name,
                    'reason': f'{param_name} should be one of this values '
                        f'({[x.name for x in enum]})',
                }] 
            )
            