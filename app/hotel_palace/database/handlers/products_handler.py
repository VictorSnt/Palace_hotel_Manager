from typing import List
from ...models import Product

class ProductHandler:
    
    @staticmethod
    def get_all_products() -> List[Product]:
        """
        Retorna uma lista de salas limit=200 default=36.
        """
        return Product.objects.all().order_by('description')
    
    @staticmethod
    def get_products_by_ids(ids: List[int]) -> List[Product]:
        """
        Retorna uma lista de salas com IDs fornecidos.
        """
        return Product.objects.filter(id__in=ids).order_by('description')
        
            
    