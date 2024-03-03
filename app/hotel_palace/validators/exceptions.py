from django.core.exceptions import ValidationError

class DBValidationError(ValidationError):
    pass

class RoomValidationError(ValidationError):
    pass
