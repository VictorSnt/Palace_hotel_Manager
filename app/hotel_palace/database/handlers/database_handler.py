from django.db.models.query import QuerySet
from django.db.models import Model
from typing import List
from uuid import UUID

from ...schemas.database_filter import DBFilter


class DataBaseHandler:
    @staticmethod
    def get_all(model_class: Model, dbfilter: DBFilter) -> QuerySet[Model]:
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
        queryset = model_class.objects.all()
        if dbfilter.order_by:
            queryset = DataBaseHandler.__order_by(queryset, dbfilter)
        else:
            queryset.order_by('-created_at')
        return queryset

    @staticmethod
    def get_by_ids(
            model_class: Model, ids: List[UUID],
            dbfilter: DBFilter
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
        queryset = model_class.objects.filter(id__in=ids)
        if dbfilter.order_by:
            queryset = DataBaseHandler.__order_by(queryset, dbfilter)
        return queryset

    @staticmethod
    def __order_by(queryset: QuerySet, dbfilter: DBFilter) -> QuerySet:
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
        return queryset.order_by(key if ascending else f'-{key}')
