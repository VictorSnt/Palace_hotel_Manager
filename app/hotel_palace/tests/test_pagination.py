from django.test import TestCase, Client
from ..models import Category, Room

class PaginationAndSortingTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_rooms()
        
    def create_rooms(self):
        category = Category.objects.get_or_create(
            description='padrão', one_guest_price=90, two_guest_price=170, 
            three_guest_price=250, four_guest_price=300
        )[0]
        for i in range(10):
            Room.objects.create(
                number=i+1, status="FREE", category=category
            )
        
    def test_pagination(self):
        # Given
        page_size = 5
        url = '/api/room'
        
        # When
        response = self.client.get(f'{url}?page_size={page_size}')
        
        # Then
        self._assert_pagination_response(response, page_size)

        # When
        next_url = response.json()['next']
        response = self.client.get(next_url)
        
        # Then
        self._assert_pagination_response(response, page_size)
        
    def test_order_by_and_ascending(self):
        # Given
        url = '/api/room'
        page_size = 5
        # When
        response = self.client.get(
            f'{url}?page=1&page_size={page_size}&order_by=number&ascending=true')
        
        # Then
        self._assert_ordered_response(response, ascending=True)

        # When
        response = self.client.get(
            f'{url}?page=1&page_size={page_size}&order_by=number&ascending=false'
        )
        
        # Then
        self._assert_ordered_response(response, ascending=False)

    def _assert_pagination_response(self, response, page_size):
        # Then
        self.assertEqual(response.status_code, 200)
        self.assertIn('count', response.json().keys())
        self.assertIn('next', response.json().keys())
        self.assertIn('previous', response.json().keys())
        self.assertIn('results', response.json().keys())
        self.assertEqual(response.json()['count'], 10)
        self.assertEqual(len(response.json()['results']), page_size)
        
    def _assert_ordered_response(self, response, ascending):
        # Then
        
        self.assertEqual(response.status_code, 200)
        rooms = response.json()['results']
        room_numbers = [room['number'] for room in rooms]
        if ascending:
            self.assertEqual(room_numbers, sorted(room_numbers))
        else:
            self.assertEqual(room_numbers, sorted(room_numbers, reverse=True))
