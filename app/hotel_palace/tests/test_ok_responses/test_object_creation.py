from django.test import TestCase, Client
from ...schemas.models.category_schemas import CategoryOutSchema
from ...schemas.models.room_schemas import RoomOutSchema
from ...schemas.models.customer_schema import CustomerOutSchema
from ...schemas.models.product_schema import ProductOutSchema
from ...schemas.models.reservation_schema import ReservationOutSchema
from ...schemas.models.accomodation_schema import AccommodationOutSchema
from ...schemas.models.consume_schema import ConsumeOutSchema


class TestObjCreation(TestCase):
    
    def setUp(self) -> None:
        self.client = Client()
        self.test_cases = [
            (
                '/api/category', 
                {  
                    "description": "standard",
                    "one_guest_price": 90,
                    "two_guest_price": 170,
                    "three_guest_price": 250,
                    "four_guest_price": 300
                },
                CategoryOutSchema
            ),
            (
                '/api/room', 
                {
                    "number": "123",
                    "status": "FREE",
                    "category": "uuid"
                },
                RoomOutSchema
            ),
            (
                '/api/customer',
                {
                    "full_name": "string",
                    "birth_date": "2000-03-11",
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
                },
                CustomerOutSchema
            ),
            (
                '/api/product',
                {
                    "description": "string",
                    "price": 0
                },
                ProductOutSchema
            ),
            (
                '/api/reservation',
                {
                    "customer_name": "string",
                    "room": "uuid",
                    "checkin_date": "2024-03-11"
                },
                ReservationOutSchema
            ),
            (
                '/api/accommodation',
                {
                    "room": "uuid",
                    "customer": "uuid",
                    "guest_quant": 1,
                    "checkin_date": "2024-03-11",
                    
                },
                AccommodationOutSchema
            ),
            (
                '/api/consume',
                {
                    "accommodation": "uuid",
                    "product": "uuid",
                    "quantity": 2,
                },
                ConsumeOutSchema
            ),
        ]
        
    def test_category_return(self):
        for url, data, schema in self.test_cases:
            self._replace_uuid_with_object_id(data)
            response = self.client.post(url, data, 'application/json')
            self.assertEqual(response.status_code, 201)
            response = self.client.get(url)
            
            self.assertTrue(
                schema(**response.json()['results'][0]), 
                f"Invalid error payload for URL: {url}"
            )
            
    def _replace_uuid_with_object_id(self, json_dict):
        for key, value in json_dict.items():
            if value == 'uuid':
                json_dict[key] = self._get_object_uuid(key)
                
    def _get_object_uuid(self, param):
        response = self.client.get(f'/api/{param}')
        return response.json()['results'][0]['id']
    