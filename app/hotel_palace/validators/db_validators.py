import json
from django.db.models.query import QuerySet
from ..validators.exceptions import DBValidationError

class DBValidator:
    @staticmethod
    def is_valid_and_not_empty_queryset(queryset: QuerySet):
        if not queryset.exists():
            error_details = {
                "type": "DBValidationError",
                "title": "No data found",
                "detail": "The database query returned no results."
            }
            raise DBValidationError(json.dumps(error_details), 404)
        