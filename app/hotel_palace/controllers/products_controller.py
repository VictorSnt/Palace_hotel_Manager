from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra, PaginatedResponseSchema
)

from ..database.handlers.database_handler import DataBaseHandler
from ..schemas.database_filter import DBFilter
from ..schemas.products_schema import ProductsSchema
from ..validators.id_validator import IDValidator
from ..validators.db_validators import DBValidator
from ..services.parsers import IDParser
from ..models import Product


@api_controller('/products', tags=['Products'])
class ProductController:
    
    @route.get('', response=PaginatedResponseSchema[ProductsSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_products(self, dbfilter: Query[DBFilter]):
        products = DataBaseHandler.get_all(Product, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(products)
        return products
    
    @route.get('/{ids}', response=PaginatedResponseSchema[ProductsSchema])
    @paginate(PageNumberPaginationExtra, page_size=36)
    def get_products_by_id(self, ids: str, dbfilter: Query[DBFilter]):
        
        IDValidator.is_valid_id_type(ids)
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        rooms = DataBaseHandler.get_by_ids(Product, parsed_ids, dbfilter)
        DBValidator.is_valid_and_not_empty_queryset(rooms)
        return rooms
    
      