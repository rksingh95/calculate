import base64
from unittest import TestCase

from app.api.v1.routes.get_calculations import router
from app.calculate import Calculator
from app.validate import validate_input
from fastapi.testclient import TestClient


class BaseClass(TestCase):
    def setUp(self) -> None:
        self.client = TestClient(router)
        self.calculation_string = "2*4-3*5"
        self.encoded_string = base64.b64encode(bytes(self.calculation_string, "utf-8"))


class TestCalculator(BaseClass):
    def setUp(self) -> None:
        super().setUp()

    def test_make_valid_calculation(self):
        result = Calculator(self.calculation_string)
        self.assertEqual(result.result, -7)

    def test_make_invalid_calculation(self):
        self.calculation_string = ""
        with self.assertRaises(IndexError):
            Calculator(self.calculation_string)

    def test_make_invalid_operations(self):
        self.calculation_string = "22*3-"
        with self.assertRaises(TypeError):
            Calculator(self.calculation_string)

    def test_make_invalid_operations_with_other_characters(self):
        self.calculation_string = "pf22*3-"
        with self.assertRaises(TypeError):
            Calculator(self.calculation_string)

    def test_make_complex_valid_operations(self):
        self.calculation_string = "22*4-(3*5)+2"
        result = Calculator(self.calculation_string)
        self.assertEqual(result.result, 58)

    def test_validate_input(self):
        result = validate_input(self.encoded_string)
        self.assertEqual(result, self.calculation_string)

    def test_get_valid_calculations(self):
        response = self.client.get("calculates/?query=Mio0LTMqNQ==")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"error": False, "result": -7.0, "message": "Result Calculated"},
        )

    def test_get_invalid_calculations(self):
        response = self.client.get("calculates/?query=123")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "error": True,
                "result": 0.0,
                "message": "Only base64 encoded strings " "accepted",
            },
        )

    def test_get_invalid_operations_calculations(self):
        response = self.client.get("calculates/?query=Mio0NQo==")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "error": True,
                "result": 0.0,
                "message": "exceptions must derive from BaseException",
            },
        )
