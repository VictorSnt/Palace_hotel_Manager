from enum import Enum
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Model
from ninja import Schema
from ..schemas.query_strings.database_filter import DBFilter
from ..validators.id_validator import IDValidator
from ..validators.db_validators import DBValidator
from ..validators.enum_validator import EnumValidator
from ..services.trasformators.parsers import IDParser


class BaseService:

    @staticmethod
    def _validate_db_field(model: Model, dbfilter: DBFilter) -> None:
        DBValidator.is_valid_db_field(model, dbfilter.order_by)

    @staticmethod
    def _validate_queryset(rooms: QuerySet) -> None:
        DBValidator.is_valid_and_not_empty_queryset(rooms)
        
    @staticmethod
    def _validate_n_parse_uuid(ids: str) -> str :
        parsed_ids = IDParser.paser_ids_by_comma(ids)
        IDValidator.is_valid_uuid(parsed_ids)
        return parsed_ids
    
    @staticmethod
    def _validate_enum(enum: Enum, attr: str, attr_name: str):
        EnumValidator.validate_enum(enum, attr, attr_name)
        
    @staticmethod    
    def _parse_schema(schema: Schema, *args) -> dict[str, Any]:
        schema_dict = schema.model_dump()
        for arg in args:
            arg = arg.first()
            arg_name = str(arg.__class__.__name__).lower()
            schema_dict[arg_name] = arg
        return schema_dict
    
    @staticmethod
    def _validate_obj_creation(response: tuple[bool, Model]) -> None:
        room_obj, is_created = response
        DBValidator.is_created_or_already_exist(is_created, room_obj)
        