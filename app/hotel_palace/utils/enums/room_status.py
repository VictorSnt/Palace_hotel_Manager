from enum import Enum

class RoomStatus(Enum):
    FREE = 'Livre'
    OCCUPIED = 'Ocupado'
    DIRTY = 'Sujo'
    MAINTENANCE = 'Manutenção'
