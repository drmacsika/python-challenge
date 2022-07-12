from unittest import TestCase

from flask import Flask
from mongoengine import connect, disconnect
from src.models import Example
from src.routes import add_routes


class TestRouteCountCalls(TestCase):
    @classmethod
    def setUpClass(cls):
        connect(
            "9fe2c4e93f654fdbb24c02b15259716c",
            uuidRepresentation="standard",
            host="mongomock://localhost",
        )

    @classmethod
    def tearDownClass(cls):
        disconnect()

    def setUp(self):
        self.app = Flask(__name__)
        add_routes(self.app)

    def test_count_route(self):
        """Test count route"""
        target_n = 6
        with self.app.test_client() as test_client:
            response = test_client.get("/count")
            self.assertDictEqual({"number_of_calls": 1}, response.json)
            for _ in range(target_n - 2):
                test_client.get("/count")
            response = test_client.get("/count")
            self.assertDictEqual({"number_of_calls": target_n}, response.json)
        self.assertEqual(target_n, Example.objects().count())
