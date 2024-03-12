import datetime
import json
from django.test import Client, TestCase


class TestServicesCreationRoutes(TestCase):
    
    def setUp(self) -> None:
        """
        Setup the test environment.
        """
        self.client = Client()
        self.test_cases = [
            ('/api/category/', 
                {  
                    "description": "standard",
                    "one_guest_price": 90,
                    "two_guest_price": 170,
                    "three_guest_price": 250,
                    "four_guest_price": 300
                }
            ),
            ('/api/room', 
                {
                    "number": "123",
                    "status": "FREE",
                    "category": "uuid"
                }
            ),
            ('/api/customer',
                {
                    "full_name": "string",
                    "birth_date": datetime.date(2000,3,30),
                    "cpf": "string",
                    "rg": "string",
                    "gender": "MALE",
                    "marital_status": "MARRIED",
                    "partner": "string",
                    "occupation": "string",
                    "occupation_company_name": "string",
                    "zip_code": "string",
                    "address_street": "string",
                    "address_number": "string",
                    "address_ref": "string",
                    "address_district": "string",
                    "address_city": "string",
                    "address_uf": "MINAS_GERAIS",
                    "phone": "string",
                    "cellphone": "string",
                    "email": "string"
                }
            ),
            ('/api/product',
                {
                    "description": "string",
                    "price": 0
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
    
    
    def test_objects_creation_when_its_all_right(self):
        
        for case in self.test_cases:
            
            url: str = case[0]
            json_dict: dict = case[1]
            if 'uuid' in json_dict.values():
                params = [
                    key for key, value in json_dict.items() 
                    if value == 'uuid'
                ]
                for param in params:
                    json_dict[param] = self._get_object_uuid(param)
            response = self.client.post(url, json_dict, 'application/json')
            #input(response.content)
            self.assertEqual(response.status_code, 201)
    
    def _get_object_uuid(self, param: str):
        response = self.client.get(f'/api/{param}')
        return response.json()['results'][0]['id']