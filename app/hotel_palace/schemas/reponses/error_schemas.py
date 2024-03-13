from typing import List
from ninja import Schema

class InvalidParams(Schema):
    name: str
    reason: str


class ErrroDetailPayload(Schema):
    type: str
    title: str
    detail: str
    invalid_params: List[InvalidParams] = None
    
class ErrorDetailed(Schema):
    error: ErrroDetailPayload
    