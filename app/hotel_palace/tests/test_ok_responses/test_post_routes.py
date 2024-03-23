from django.test import Client, TestCase

from ...models import Accommodation, Room
from ...schemas.reponses.error_schemas import ErrorDetailed


class TestServicesPOSTRoutes(TestCase):
    
    def setUp(self) -> None:
        
        """
        Setup the test environment.
        """
        self.client = Client()
        self.error_schema = ErrorDetailed
        self.test_cases = [
            ('/api/category', 
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
                    "status": "Livre",
                    "category_id": "uuid"
                }
            ),
            ('/api/customer',
                {
                    "full_name": "string",
                    "birth_date": "2000-03-11",
                    "cpf": "string",
                    "rg": "string",
                    "gender": "Masc",
                    "marital_status": "Casado(a)",
                    "partner": "string",
                    "occupation": "string",
                    "occupation_company_name": "string",
                    "zip_code": "string",
                    "address_street": "string",
                    "address_number": "string",
                    "address_ref": "string",
                    "address_district": "string",
                    "address_city": "string",
                    "address_uf": "MG",
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
                    "room_id": "uuid",
                    "checkin_date": "2024-03-11"
                }
            ),
            ('/api/accommodation',
                {
                    "room_id": "uuid",
                    "customer_id": "uuid",
                    "guest_quant": '1',
                    "checkin_date": "2024-03-11",
                }
            ),
            ('/api/consume',
                {
                    "accommodation_id": "uuid",
                    "product_id": "uuid",
                    "quantity": '2',
                }
            ),
        ]
        
    
    def test_objects_creation_when_its_all_right_and_conflict(self):
        self._create_test_objects()
        self._test_conflict_error_payload()
    
    
    def _create_test_objects(self):
        for url, json_dict in self.test_cases:
            self._replace_uuid_with_object_id(json_dict)
            response = self.client.post(url, json_dict, 'application/json')
            input(response.content)
            self.assertEqual(
                
                response.status_code, 201, 
                f"Failed to create object for URL: {url}"
            )
            
    def _test_conflict_error_payload(self):
        for url, json_dict in self.test_cases:
            self._replace_uuid_with_object_id(json_dict)
            response = self.client.post(url, json_dict, 'application/json')
            if url == '/api/accommodation':
                self.assertEqual(
                response.status_code, 400, 
                f"Expected status code 400 for URL: {url}"
            )
            elif url == '/api/consume':
                self.assertEqual(
                response.status_code, 201, 
                f"Expected status code 400 for URL: {url}"
            )
            else:
                self.assertEqual(
                    response.status_code, 409, 
                    f"Expected status code 409 for URL: {url}"
                )
                self.assertTrue(
                    self.error_schema(**response.json()), 
                    f"Invalid error payload for URL: {url}"
                )
        
    def _replace_uuid_with_object_id(self, json_dict):
        for key, value in json_dict.items():
            if value == 'uuid':
                json_dict[key] = self._get_object_uuid(key)
    
    def _get_object_uuid(self, param):
        response = self.client.get(f'/api/{param}')
        return response.json()['results'][0]['id']
