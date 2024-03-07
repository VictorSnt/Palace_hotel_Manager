from django.test import TestCase, Client
from .factory.room_factory import RoomFactory
from .models import Room
import json

class TestRoomServices(TestCase):
    def setUp(self):
        self.client = Client()
    
    def create_rooms(self):
        RoomFactory.create_batch(10)
    
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