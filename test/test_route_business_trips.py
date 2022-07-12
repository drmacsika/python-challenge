from unittest import TestCase

from flask import Flask
from mongoengine import connect, disconnect
from src.routes import add_routes


class TestCalculate(TestCase):
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

        self.payload = {
            "name": "Alanto",
            "destinations": ["Kinganru", "Facenianorth", "SantaTiesrie"],
            "business": True,
            "distances": [
                "Munich - Munich: 0",
                "Munich - Kinganru: 3",
                "Munich - Facenianorth: 7",
                "Munich - SantaTiesrie: 4",
                "Munich - Mitling: 1",
                "Kinganru - Facenianorth: 2",
                "Kinganru - SantaTiesrie: 1",
                "Kinganru - Mitling: 1",
                "Facenianorth - SantaTiesrie: 5",
                "Facenianorth - Mitling:  3",
                "SantaTiesrie - Mitling: 2",
            ],
        }

    def test_business_trips_disallow_post_update_delete_request_methods(self):
        """Test ensure other http methods are not allowed"""
        with self.app.test_client() as test_client:
            response = test_client.post("/business-trips")
            self.assertEqual(response.status_code, 405)
            response = test_client.put("/business-trips")
            self.assertEqual(response.status_code, 405)
            response = test_client.patch("/business-trips")
            self.assertEqual(response.status_code, 405)
            response = test_client.delete("/business-trips")
            self.assertEqual(response.status_code, 405)

    def test_business_trips_post_request(self):
        """Test ensure only http GET method"""
        with self.app.test_client() as test_client:
            response = test_client.get("/business-trips")
            self.assertEqual(response.status_code, 201)

    def test_business_trips_response(self):
        """Test ensure response is correct"""
        with self.app.test_client() as test_client:
            for _ in range(3):
                test_client.post("/calculate", json=self.payload)
            response = test_client.get("/business-trips")
            self.assertDictEqual(
                response.get_json(),
                {
                    "penguins_with_most_trips": ["Alanto"],
                    "most_visited_places": ["Kinganru", "Facenianorth", "SantaTiesrie"],
                    "total_business_trips": 3,
                },
            )
