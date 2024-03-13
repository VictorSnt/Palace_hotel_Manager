from django.test import TestCase, Client
from ...schemas.reponses.error_schemas import ErrorDetailed

class TestPostErrorPayloads(TestCase):
    
    def setUp(self) -> None:
        self.client = Client()
        self.error_schema = ErrorDetailed
    
        self.test_cases = [
            
            ('/api/room', 
                {
                    "number": "123",
                    "status": "FREE",
                    "category": "uuid"
                }
            ),
            ('/api/reservation',
                {
                    "customer_name": "string",
                    "room": "uuid",
                    "checkin_date": "2024-03-11"
                }
            ),
            ('/api/accommodation',
                {
                    "room": "uuid",
                    "customer": "uuid",
                    "guest_quant": 1,
                    "is_active": True,
                    "days_quant": 1,
                    "checkin_date": "2024-03-11",
                    "checkout_date": "2024-03-11",
                    "checkin_time": "23:36:15",
                    "checkout_time": "23:36:15",
                    "hosting_price": 150,
                    "total_hosting_price": 150,
                    "total_bill": 150
                }
            ),
            ('/api/consume',
                {
                    "accommodation": "uuid",
                    "room": "uuid",
                    "product": "uuid",
                    "quantity": 2,
                    "unit_price": 2,
                    "total": 4
                }
            ),
        ]
        
    def test_room_creation_with_invalid_params_payload(self):
        for url, wrong_params in self.test_cases:
            response = self.client.post(
                url, 
                wrong_params, 
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 422)
            self.assertTrue(self.error_schema(**response.json()))
      
    