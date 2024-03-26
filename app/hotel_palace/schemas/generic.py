from typing import List
from uuid import UUID
from ninja import Schema

class IdList(Schema):
    ids: List[UUID]
