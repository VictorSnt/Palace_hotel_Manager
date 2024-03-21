from django.db.models.query import QuerySet
from django.db.models import Model

from typing import List
from uuid import UUID
from ...services.errors.exceptions import IntegrityError
from ...schemas.query_strings.database_filter import DBFilter


class DataBaseHandler:
    @staticmethod
    def get_all(
        model_class: Model, 
        dbfilter: DBFilter = None
        ) -> QuerySet[Model]:
        """
        Retorna uma queryset de todas as instâncias do modelo especificado.

        Parâmetros:
        - model_class: Classe do modelo Django.
        - dbfilter: Argumentos opcionais.
            - 'order_by' (opcional, padrão created_at): 
                Campo de ordenação para a queryset.
                Exemplo: 'order_by="nome"' (ordenação pelo campo 'nome').
            
            - 'ascending' (opcional, padrão True): 
                Define se ordenação é ascendente (True) ou descendente (False).

        Retorna:
        Uma queryset contendo todas as instâncias do modelo,
        opcionalmente ordenada.
        """
        key = '-created_at' #padrão
        queryset = model_class.objects.all()
        if dbfilter and dbfilter.order_by:
            key = DataBaseHandler.__order_by(dbfilter)
        return queryset.order_by(key)

    @staticmethod
    def get_by_ids(
            model_class: Model, ids: List[UUID],
            dbfilter: DBFilter = None
        ) -> QuerySet[Model]:
        """
        Retorna uma queryset de instâncias do modelo especificado com IDs 
        fornecidos, opcionalmente ordenada.

        Parâmetros:
        - model_class: Classe do modelo Django.
        - ids: Lista de UUIDs das instâncias a serem recuperadas.
        - dbfilter: Argumentos opcionais.
            - 'order_by' (opcional, padrão created_at): 
                Campo de ordenação para a queryset.
                Exemplo: 'order_by="nome"' (ordenação pelo campo 'nome').
            
            - 'ascending' (opcional, padrão True): 
                Define se ordenação é ascendente (True) ou descendente (False).
        Retorna:
        Uma queryset contendo todas as instâncias do modelo,
        opcionalmente ordenada.
        """
        key = '-created_at' #padrão
        queryset = model_class.objects.filter(id__in=ids)
        if dbfilter and dbfilter.order_by:
            key = DataBaseHandler.__order_by(dbfilter)
        return queryset.order_by(key)

            
    @staticmethod
    def try_to_create(
        model_class: Model, 
        model_schema: dict,
        allow_dups=False
        ) -> tuple[Model, bool]:
        try:
            if allow_dups:
                return model_class.objects.create(**model_schema), True
            else:
                return model_class.objects.get_or_create(**model_schema)
                
        except IntegrityError:
            unique_field_name = [
                field.name for field in model_class._meta.fields 
                if field.unique and field.name in model_schema.keys()
            ][0]
            query = {unique_field_name: model_schema[unique_field_name]}
            existing_instance = model_class.objects.filter(**query).first()
            return existing_instance, False
        
        
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
