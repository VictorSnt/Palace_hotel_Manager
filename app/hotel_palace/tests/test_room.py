from django.test import TestCase, Client

class TestHotelServices(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_get_rooms_when_no_data_in_database(self):
        response = self.client.get(
            '/api/room',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)
        
    def test_get_room_by_id_when_uuid_is_invalid(self):
        invalid_uuid = 1
        response = self.client.get(
            f'/api/room/{invalid_uuid}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 422)

    def test_get_categories(self):
        response = self.client.get(
            '/api/category',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)
        
    def test_get_category_by_ids_when_ids_are_invalid(self):
        invalid_ids = '1,2,3'
        response = self.client.get(
            f'/api/category/{invalid_ids}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 422)
        
    def test_get_consumes(self):
        response = self.client.get(
            '/api/consume',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)
        
    def test_get_consumes_by_ids_when_ids_are_invalid(self):
        invalid_ids = '1,2,3'
        response = self.client.get(
            f'/api/consume/{invalid_ids}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 422)
        
    def test_get_products(self):
        response = self.client.get(
            '/api/products',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)
        
    def test_get_products_by_ids_when_ids_are_invalid(self):
        invalid_ids = '1,2,3'
        response = self.client.get(
            f'/api/products/{invalid_ids}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 422)
        
    def test_get_customers(self):
        response = self.client.get(
            '/api/customer',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)
        
    def test_get_customers_by_ids_when_ids_are_invalid(self):
        invalid_ids = '1,2,3'
        response = self.client.get(
            f'/api/customer/{invalid_ids}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 422)
    
    def test_get_accommodations(self):
        response = self.client.get(
            '/api/accommodation',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)
        
    def test_get_accommodations_by_ids_when_ids_are_invalid(self):
        invalid_ids = '1,2,3'
        response = self.client.get(
            f'/api/accommodation/{invalid_ids}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 422)
        
    def test_get_reservations(self):
        response = self.client.get(
            '/api/reservation',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)
        
    def test_get_reservations_by_ids_when_ids_are_invalid(self):
        invalid_ids = '1,2,3'
        response = self.client.get(
            f'/api/reservation/{invalid_ids}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 422)