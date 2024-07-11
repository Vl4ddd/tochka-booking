from django.test import TestCase

# Create your tests here.

class TestHotels(TestCase):

   
    def test_index(self):
        response = self.client.get('/hotels/')
        self.assertEqual(response.status_code, 200)
