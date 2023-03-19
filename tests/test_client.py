import lotr
import os
import unittest

API_KEY = os.getenv('LOTR_API_KEY')


class TestClient(unittest.TestCase):
    def test_api_key(self):
        client = lotr.Client(API_KEY)
        client.get_movies()