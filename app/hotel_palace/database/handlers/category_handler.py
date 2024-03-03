from typing import List
from ...models import RoomCategory

class CategoryHandler:
    
    @staticmethod
    def get_all_categories() -> List[RoomCategory]:
        """
        Retorna uma lista de salas limit=200 default=36.
        """
        return RoomCategory.objects.all().order_by('description')
    
    @staticmethod
    def get_categories_by_ids(ids: List[int]) -> List[RoomCategory]:
        """
        Retorna uma lista de salas com IDs fornecidos.
        """
        
        return RoomCategory.objects.filter(id__in=ids).order_by('description')
        
            
    