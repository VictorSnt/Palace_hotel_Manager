from uuid import UUID
from ninja import Schema


class SuccessDetailed(Schema):
   message: str
   id: UUID = None