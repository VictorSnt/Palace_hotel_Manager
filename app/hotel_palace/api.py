from ninja_extra import NinjaExtraAPI
from .validators.exceptions import DBValidationError, RoomValidationError
from .controllers.room_controller import RoomController
from .handlers.exception_handlers import validation_exception


api = NinjaExtraAPI()
api.add_exception_handler(DBValidationError, validation_exception)
api.add_exception_handler(RoomValidationError, validation_exception)
api.register_controllers(RoomController)
