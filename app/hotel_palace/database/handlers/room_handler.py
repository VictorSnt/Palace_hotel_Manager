from typing import List
from uuid import UUID
from ...models import Room

class RoomHandler:
    
    @staticmethod
    def get_all_rooms() -> List[Room]:
        """
        Retorna uma lista de salas limit=200 default=36.
        """
        return Room.objects.all().order_by('number')
    
    @staticmethod
    def get_rooms_by_ids(ids: List[UUID]) -> List[Room]:
        """
        Retorna uma lista de salas com IDs fornecidos.
        """
        
        return Room.objects.filter(id__in=ids).order_by('number')
        
            
    