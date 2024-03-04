from typing import List
from uuid import UUID
from ...models import Customer

class CustomerHandler:
    
    @staticmethod
    def get_all_cutomers() -> List[Customer]:
        """
        Retorna uma lista de clientes limit=200 default=36.
        """
        return Customer.objects.all().order_by('full_name')
    
    @staticmethod
    def get_cutomers_by_ids(ids: List[UUID]) -> List[Customer]:
        """
        Retorna uma lista de clientes com IDs fornecidos.
        """
        
        return Customer.objects.filter(id__in=ids).order_by('full_name')
        
            
    