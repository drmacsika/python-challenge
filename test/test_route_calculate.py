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

        self.sample_response = {
            "places_to_travel": [
                "Munich",
                "Mitling",
                "Kinganru",
                "Facenianorth",
                "Kinganru",
                "SantaTiesrie",
            ]
        }

    def test_calculate_disallow_get_update_delete_request_methods(self):
        """Test ensure other http methods are not allowed"""
        with self.app.test_client() as test_client:
            response = test_client.get("/calculate")
            self.assertEqual(response.status_code, 405)
            response = test_client.put("/calculate")
            self.assertEqual(response.status_code, 405)
            response = test_client.patch("/calculate")
            self.assertEqual(response.status_code, 405)
            response = test_client.delete("/calculate")
            self.assertEqual(response.status_code, 405)

    def test_calculate_empty_post_request(self):
        """Test ensure POST can't be called without a payload"""
        with self.app.test_client() as test_client:
            response = test_client.post("/calculate")
            self.assertEqual(response.status_code, 400)

    def test_calculate_post_request(self):
        """Test ensure only http POST methods allowed with payload"""
        with self.app.test_client() as test_client:
            response = test_client.post("/calculate", json=self.payload)
            self.assertEqual(response.status_code, 201)

    def test_calculate_validate_incomplete_payload(self):
        """Test ensure payload is not incomplete"""
        with self.app.test_client() as test_client:
            response = test_client.post("/calculate", json={"name": "Alanto"})
            self.assertEqual(response.status_code, 405)

    def test_calculate_validate_empty_payload(self):
        """Test ensure payload is not empty"""
        with self.app.test_client() as test_client:
            response = test_client.post("/calculate", json={})
            self.assertEqual(response.status_code, 405)

    def test_calculate_validate_invalid_field_payload(self):
        """Test ensure only only valid fields in payload"""
        with self.app.test_client() as test_client:
            response = test_client.post(
                "/calculate", json=self.payload.update({"test": "test"})
            )
            self.assertNotEqual(response.status_code, 201)

    def test_calculate_response(self):
        """Test ensure POST returns correct response"""
        with self.app.test_client() as test_client:
            response = test_client.post("/calculate", json=self.payload)
            self.assertDictEqual(response.json, self.sample_response)
