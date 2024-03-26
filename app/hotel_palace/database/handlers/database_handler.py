import json
from django.db.models.query import QuerySet
from django.db.models import Model
from uuid import UUID
from django.shortcuts import get_list_or_404, get_object_or_404
from ...services.errors.exceptions import IntegrityError, ValidationError
from ...schemas.query_strings.database_filter import DBFilter


class DataBaseHandler:
    @staticmethod
    def get_all(model_class: Model, dbfilter: DBFilter)-> QuerySet:
        key = '-created_at' #padrão
        queryset = model_class.objects.all()
        if dbfilter and dbfilter.order_by:
            key = DataBaseHandler.__order_by(dbfilter)
        return queryset.order_by(key)

    @staticmethod
    def get_by_id(model_class: Model, id: UUID) -> Model:
        obj = get_object_or_404(model_class, pk=id)
        return obj
    
    @staticmethod
    def get_by_ids(model_class: Model, ids, dbfilter: DBFilter)-> QuerySet:
        key = 'created_at'
        obj_list = get_list_or_404(model_class, id__in=ids)
        if dbfilter and dbfilter.order_by:
            sort_filter = {
                'key': lambda x: getattr(x, dbfilter.order_by),
                'reverse': not dbfilter.ascending
            }
            obj_list = sorted(obj_list, **sort_filter)
        return obj_list
    
    @staticmethod
    def create(model_class: Model, model_schema: dict) -> UUID:
        try:
            return model_class.objects.create(**model_schema).id
        except IntegrityError as e:
            message = json.dumps({'detail': str(e)})
            raise ValidationError(message, 409)
            
    @staticmethod
    def update(obj: Model, props: dict):
        try:
            for key, value in props.items():
                if value:
                    setattr(obj, key, value)
            obj.save()
        except IntegrityError as e:
            message = json.dumps({'detail': str(e)})
            raise ValidationError(message, 409)
    
    @staticmethod
    def __order_by(dbfilter: DBFilter) -> QuerySet:
        """
        Ordena uma queryset de acordo com os parâmetros fornecidos.

        Parâmetros:
        - queryset: Queryset a ser ordenada.
        - dbfilter: Argumentos opcionais. Pode incluir 
            'order_by' (campo de ordenação) e 
            'ascending' (ordem ascendente ou descendente).

        Retorna:
        A queryset ordenada.
        """
        key = dbfilter.order_by
        ascending = dbfilter.ascending
        return key if ascending else f'-{key}'
