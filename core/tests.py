from django.test import TestCase
from django.test.client import Client


class CoreTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_url_registering_url_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
