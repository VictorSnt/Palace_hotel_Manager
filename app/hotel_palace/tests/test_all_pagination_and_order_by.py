from django.test import TestCase, Client
from ..factory import factories as db_factory

class RoomPaginationAndSortingTest(TestCase):
    """
    Test pagination and ordering of application entities.
    """

    def setUp(self):
        """
        Setup the test environment.
        """
        self.client = Client()
        self.expected_rows_count = 15
        self.seed_database(self.expected_rows_count)
        self.test_cases = [
            ('/api/room', 5, 'number', True),
            ('/api/room', 5, 'number', False),
            ('/api/category', 5, 'description', True),
            ('/api/category', 5, 'description', False),
            ('/api/customer', 5, 'full_name', True),
            ('/api/customer', 5, 'full_name', False),
            ('/api/accommodation', 5, 'guest_quant', True),
            ('/api/accommodation', 5, 'guest_quant', False),
            ('/api/consume', 5, 'total', True),
            ('/api/consume', 5, 'total', False),
            ('/api/reservation', 5, 'customer_name', True),
            ('/api/reservation', 5, 'customer_name', False),
        ]
        
        
    def test_pagination_and_ordering(self):
        """
        Test pagination and ordering for different API endpoints.
        """
        # Define test cases for different endpoints, page sizes,
        # ordering fields, and ordering directions.
        

        # Iterate over each test case.
        for url, page_size, order_by, ascending in self.test_cases:
            with self.subTest(
                url=url, page_size=page_size, order_by=order_by, 
                ascending=ascending):
                # Given: The scenario where pagination and ordering works.
                # Arrange: Prepare the request parameters.
                params = {
                    'page_size': page_size,
                    'order_by': order_by,
                    'ascending': ascending,
                }
                # When: Making a GET request to the specified URL.
                response = self.client.get(url, params)
                # Then: Verify if the API response is correct.
                self._assert_pagination_response(response, page_size)
                self._assert_ordered_response(response, order_by, ascending)

    # Private methods to verify the API response.
    def _assert_pagination_response(self, response, page_size):
        """
        Verify if the API response contains the expected pagination elements.
        """
        response_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('count', response_data)
        self.assertIn('next', response_data)
        self.assertIn('previous', response_data)
        self.assertIn('results', response_data)
        # Verify if the number of results matches the specified page size.
        self.assertEqual(response_data['count'], self.expected_rows_count)
        self.assertEqual(len(response_data['results']), page_size)
        
    def _assert_ordered_response(self, response, order_by, ascending):
        """
        Verify if the results are correctly ordered.
        """
        response_data = response.json()
        self.assertEqual(response.status_code, 200)
        rooms = response_data['results']
        room_numbers = [room[order_by] for room in rooms]
        # Verify if the results are ordered correctly.
        if ascending:
            self.assertEqual(room_numbers, sorted(room_numbers))
        else:
            self.assertEqual(room_numbers, sorted(room_numbers, reverse=True))

    # Method to generate test data in the database.
    def seed_database(self, data_quant):
        """
        Generate test data in the database.
        """
        db_factory.CategoryFactory.create_batch(data_quant)
        db_factory.RoomFactory.create_batch(data_quant)
        db_factory.CustomerFactory.create_batch(data_quant)
        db_factory.ProductFactory.create_batch(data_quant)
        db_factory.ReservationFactory.create_batch(data_quant)
        db_factory.AccommodationFactory.create_batch(data_quant)
        db_factory.ConsumeFactory.create_batch(data_quant)
