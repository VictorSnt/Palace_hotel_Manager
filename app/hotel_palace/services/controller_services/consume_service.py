from ...models import Consume
from ...database.handlers.database_handler import DataBaseHandler
from ...services.base_service import BaseService

class ConsumeService(BaseService):
    
    @staticmethod
    def delete(model, id):
        obj: Consume = DataBaseHandler.get_by_id(model, id)
        accommo = obj.accommodation
        accommo.total_bill -= obj.total
        accommo.save()
        DataBaseHandler.delete(obj)
        return 200, {'message': 'Deletado com sucesso'}  
        
    @staticmethod
    def _parse_accommodation_info(obj: dict):
        total_bill = float(obj['accommodation'].total_bill)
        total_bill += obj['total']
        obj['accommodation'].total_bill = total_bill
        obj['accommodation'].save()
        