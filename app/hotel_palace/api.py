from .controllers.room_controller import RoomController
from ninja_extra import NinjaExtraAPI

api = NinjaExtraAPI()
api.register_controllers(RoomController)