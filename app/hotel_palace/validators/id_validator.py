import json
from uuid import UUID
from ..validators.exceptions import RoomValidationError

class IDValidator:
    @staticmethod
    def is_valid_id_type(id: str) -> None:
        if not isinstance(id, str):
            error_details = {
                "type": "RoomValidationError",
                "title": "Your request parameters didn't validate.",
                "invalid-params": [ 
                    {
                        "name": "id",
                        "reason": "must be a string"
                    },
                ]
            }
            raise RoomValidationError(json.dumps(error_details), 422)

    @staticmethod
    def is_valid_uuid(ids: list[str]) -> None: 
        if not isinstance(ids, list):
            error_details = {
                "type": "RoomValidationError",
                "title": "Your request parameters didn't validate.",
                "invalid-params": [ 
                    {
                        "name": "ids",
                        "reason": "must be a list with one or more UUIDs"
                    },
                ]
            }
            raise RoomValidationError(json.dumps(error_details), 422)
        
        try:
            for id in ids:
                UUID(id)
        except ValueError as e:
            error_details = {
                "type": "RoomValidationError",
                "title": "Your request parameters didn't validate.",
                "invalid-params": [ 
                    {
                        "name": "id",
                        "reason": "must be a UUID format string"
                    },
                ]
            }
            raise RoomValidationError(json.dumps(error_details), 422)
