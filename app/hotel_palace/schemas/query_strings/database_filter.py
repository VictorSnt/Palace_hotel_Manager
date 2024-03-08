from types import NoneType
from ninja import Schema

class DBFilter(Schema):
    order_by: str|NoneType = None
    ascending: bool = True
