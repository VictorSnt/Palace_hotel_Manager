import json
from ...validators.exceptions import ValidationError

class ErrorPayloadGenerator:
    @staticmethod
    def generate_error_payload(
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
        