# calculator/tests.py

import unittest
from pkg.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """
    Unit tests for the Calculator class.
    Covers basic arithmetic, nested expressions, and error handling.
    """
    def setUp(self):
        # Initialize a Calculator instance before each test
        self.calculator = Calculator()

    # Basic arithmetic tests
    def test_addition(self):
        result = self.calculator.evaluate("3 + 5")
        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = self.calculator.evaluate("10 - 4")
        self.assertEqual(result, 6)

    def test_multiplication(self):
        result = self.calculator.evaluate("3 * 4")
        self.assertEqual(result, 12)

    def test_division(self):
        result = self.calculator.evaluate("10 / 2")
        self.assertEqual(result, 5)

    # Test nested expressions to ensure proper operator precedence
    def test_nested_expression(self):
        result = self.calculator.evaluate("3 * 4 + 5")
        self.assertEqual(result, 17)

    # Test more complex expression combining multiple operators
    def test_complex_expression(self):
        result = self.calculator.evaluate("2 * 3 - 8 / 2 + 5")
        self.assertEqual(result, 7)

    # Handle edge case: empty input should return None
    def test_empty_expression(self):
        result = self.calculator.evaluate("")
        self.assertIsNone(result)

    # Handle invalid operators by raising a ValueError
    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("$ 3 5")

    # Handle malformed expressions with insufficient operands
    def test_not_enough_operands(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("+ 3")


if __name__ == "__main__":
    unittest.main()