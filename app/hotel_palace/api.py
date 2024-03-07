from ninja_extra import NinjaExtraAPI
from .validators.exceptions import (
  ValidationError ,DBValidationError, RoomValidationError)
from .controllers.room_category_controller import RoomCategoryController
from .controllers.products_controller import ProductController
from .controllers.customer_controller import CustomerController
from .controllers.room_controller import RoomController
from .controllers.accommodation_controller import AccommodationController
from .controllers.product_consume_controller import ProductConsumeController
from .handlers.exception_handlers import exception_handler

api = NinjaExtraAPI()
api.add_exception_handler(DBValidationError, exception_handler)
api.add_exception_handler(RoomValidationError, exception_handler)
api.add_exception_handler(ValidationError, exception_handler)
api.register_controllers(RoomCategoryController)
api.register_controllers(RoomController)
api.register_controllers(ProductController)
api.register_controllers(CustomerController)
api.register_controllers(ProductConsumeController)
api.register_controllers(AccommodationController)

