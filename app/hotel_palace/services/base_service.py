from enum import Enum
from typing import Any, Tuple
from django.db.models.query import QuerySet
from django.db.models import Model
from django.shortcuts import get_object_or_404
from ninja import Schema

from ..database.handlers.database_handler import DataBaseHandler
from ..schemas.query_strings.database_filter import DBFilter
from ..validators.id_validator import IDValidator
from ..validators.db_validators import DBValidator
from ..validators.enum_validator import EnumValidator
from ..services.trasformators.parsers import IDParser
from ..schemas.reponses.success_schemas import SuccessDetailed


class BaseService:
    
    Success201  = Tuple[int, SuccessDetailed]
    
    @staticmethod
    def get_all(model: Model, dbfilter: DBFilter) -> QuerySet:
        BaseService._validate_db_field(model, dbfilter)
        reservations = DataBaseHandler.get_all(model, dbfilter)
        BaseService._validate_queryset(reservations)
        return reservations
    
    @staticmethod
    def get_by_id(model: Model, id: str) -> Model: 
        obj = DataBaseHandler.get_by_id(model, id)
        return obj
    
    @staticmethod
    def get_by_ids(model: Model, ids: list, dbfilter: DBFilter) -> Model: 
        obj = DataBaseHandler.get_by_ids(model, ids, dbfilter)
        return obj
    
    @staticmethod
    def create(model: Model, model_schema: Schema) -> Success201:
        args = model, model_schema.model_dump()
        obj_id = DataBaseHandler.create(*args)
        return 201, {'message': 'Criado com sucesso', 'id': obj_id}
    
    @staticmethod
    def update(model, id, update_schema: Schema):
        obj = DataBaseHandler.get_by_id(model, id)
        DataBaseHandler.update(obj, update_schema.model_dump())
        return 200, {'message': 'Atualizado com sucesso'}

    @staticmethod
    def delete(model, id):
        obj = DataBaseHandler.get_by_id(model, id)
        DataBaseHandler.delete(obj)
        return 200, {'message': 'Deletado com sucesso'}

    @staticmethod
    def get_obj_backref(model, id, key):
        obj = DataBaseHandler.get_by_id(model, id)
        return getattr(obj, key).all()
    
    @staticmethod
    def _validate_db_field(model: Model, dbfilter: DBFilter) -> None:
        if dbfilter and dbfilter.order_by: 
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
        if args:
            for arg in args:
                arg = arg.first()
                arg_name = str(arg.__class__.__name__).lower()
                schema_dict[arg_name] = arg
        return schema_dict
    
    @staticmethod
    def _validate_obj_creation(response: tuple[bool, Model]) -> None:
        room_obj, is_created = response
        DBValidator.is_created_or_already_exist(is_created, room_obj)
    