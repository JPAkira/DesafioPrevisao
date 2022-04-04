import unittest
from app import app
from dao import db
from cache import cache


class FlaskTestCase(unittest.TestCase):
    def test_temperature_city(self):
        db.init_app(app)
        cache.init_app(app)
        tester = app.test_client(self)
        response = tester.get("/temperature/london")
        statuscode = response.status_code
        self.assertEqual(statuscode, 201)

    def test_temperature_without_city(self):
        db.init_app(app)
        tester = app.test_client(self)
        response = tester.get("/temperature/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)

    def test_temperature_last_city(self):
        db.init_app(app)
        cache.init_app(app)
        tester = app.test_client(self)
        response1 = tester.get("/temperature/london")
        last_response = tester.get("/temperature?max=1")

        self.assertEqual(last_response.status_code, 201)
    
if __name__ == "__main__":
    unittest.main()