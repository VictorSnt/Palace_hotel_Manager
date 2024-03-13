import json
from .exceptions import ValidationError

class ErrorPayloadGenerator:
    
    @staticmethod
    def generate_422_error_detailed(
        exc: ValidationError,
        status_code: int,
        type: str,
        title: str,
        detail: str,
        invalid_params: list = None
        ) -> None:
        
        error_json = {
            'error': {
                'type': type,
                'title': title,
                'detail': detail,
            }
        }
        if invalid_params:
            error_json['error']['invalid-params'] = invalid_params 
        error_json = json.dumps(error_json, indent=4)
        raise exc(error_json, status_code)
        
    # @staticmethod
    # def generate_db_related_error(
    #     exc: ValidationError,
    #     status_code: int,
    #     type: str,
    #     title: str,
    #     detail: str,) -> None:
        
    #     error_json = {
    #         'error': {
    #             'type': type,
    #             'title': title,
    #             'detail': detail,
    #         }
    #     }
    #     error_json = json.dumps(error_json, indent=4)
    #     raise exc(error_json, status_code)
