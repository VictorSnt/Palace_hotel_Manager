from ninja import Path
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)

from ..database.handlers.products_handler import ProductHandler
from ..schemas.products_schema import ProductsSchema
from ..services.parsers import IDParser
from ..validators.id_validator import IDValidator
from ..validators.db_validators import DBValidator


@api_controller('/products', tags=['Products'])
class ProductController:
    
    @route.get('', response=PaginatedResponseSchema[ProductsSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_products(self):
        products = ProductHandler.get_all_products()
        DBValidator.is_valid_and_not_empty_queryset(products)
        return products
    
    @route.get('/{ids}', response=PaginatedResponseSchema[ProductsSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_products_by_id(self, ids: str = Path(
        ..., description="Lista de IDs separados por vírgula"
        )):
        
        IDValidator.is_valid_id_type(ids)
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        rooms = ProductHandler.get_products_by_ids(parsed_ids)
        DBValidator.is_valid_and_not_empty_queryset(rooms)
        return rooms
    
      