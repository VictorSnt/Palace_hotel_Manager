from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

class DBValidationError(ValidationError):
    pass

class RoomValidationError(ValidationError):
    pass

class DoesNotExistError(ValidationError):
    pass
