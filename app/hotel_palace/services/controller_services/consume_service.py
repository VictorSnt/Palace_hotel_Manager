from ...services.base_service import BaseService

class ConsumeService(BaseService):
        
    @staticmethod
    def _parse_accommodation_info(obj: dict):
        total_bill = float(obj['accommodation'].total_bill)
        total_bill += obj['total']
        obj['accommodation'].total_bill = total_bill
        obj['accommodation'].save()
        