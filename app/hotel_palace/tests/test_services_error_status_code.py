from django.test import TestCase, Client


class TestHotelServicesErrorStatusCode(TestCase):
    def setUp(self):
        self.client = Client()

    def _send_get_request(self, url):
        """
        Helper method to send a GET request and return the response.
        """
        return self.client.get(url, content_type='application/json')

    def test_all_get_endpoints(self):
        # Give
        """
        Given a scenario where the database query retuned nothing or
        the given id is a invalid uuid
        """
        # Arrange
        arrange_list = [
        ('/api/room', 404), # no results
        ('/api/room/1', 422), # wrong uuid
        ('/api/category', 404), # no results
        ('/api/category/1,2,3', 422), # wrong uuid
        ('/api/consume', 404), # no results
        ('/api/consume/1,2,3', 422), # wrong uuid
        ('/api/product', 404), # no results
        ('/api/product/1,2,3', 422), # wrong uuid
        ('/api/customer', 404), # no results
        ('/api/customer/1,2,3', 422), # wrong uuid
        ('/api/accommodation', 404), # no results
        ('/api/accommodation/1,2,3', 422), # wrong uuid
        ('/api/reservation', 404), # no results
        ('/api/reservation/1,2,3', 422), # wrong uuid
        ] 
        # Act
        for arrange in arrange_list:
            url, expected_status_code = arrange
            response = self._send_get_request(url)
            
            # Assert
            self.assertEqual(response.status_code, expected_status_code)
