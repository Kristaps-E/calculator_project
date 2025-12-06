import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a Calculator instance before each test."""
        self.calculator = Calculator()

    def test_add(self):
        """Test basic addition."""
        result = self.calculator.add(5, 3.5)
        self.assertEqual(result, 8.5)

    def test_sub(self):
        """Test basic subtraction."""
        result = self.calculator.sub(5, 3)
        self.assertEqual(result, 2)

    def test_mul(self):
        """Test basic multiplication."""
        result = self.calculator.mul(5.5, 3)
        self.assertEqual(result, 16.5)

    def test_div(self):
        """Test basic division."""
        result = self.calculator.div(6, 3)
        self.assertEqual(result, 2)

    def test_div_by_zero(self):
        """Test division by zero."""
        with self.assertRaises(ValueError):
            self.calculator.div(5, 0)

    def test_sqrt(self):
        """Test square root of positive number."""
        result = self.calculator.sqrt(25)
        self.assertEqual(result, 5)

    def test_sqrt_with_negative(self):
        """Test square root of a negative number."""
        with self.assertRaises(ValueError):
            self.calculator.sqrt(-25)

    def test_handle_square_operations(self):
        """Test handling of square root operations."""
        response = self.calculator.handle_square_operations("V 25")
        self.assertEqual(response, "The square root is: 5.0")

        self.calculator.memory = 10
        response = self.calculator.handle_square_operations("+ V 36")
        self.assertEqual(response, "The result is: 16.0")

    def test_invalid_operator(self):
        """Test arithmetic with invalid operator."""
        response = self.calculator.handle_arithmetic("! 5")
        self.assertIsNone(response)

    def test_invalid_input(self):
        """Test invalid input format."""
        response = self.calculator.handle_arithmetic("5")
        self.assertIsNone(response)


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCalculator)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    total = result.testsRun
    failed = len(result.failures)
    errors = len(result.errors)
    skipped = len(result.skipped)
    passed = total - failed - errors - skipped

    print("\n----------------------------")
    print("Test Summary:")
    print(f"Total tests: {total}")
    print(f"Passed:      {passed}")
    print(f"Failed:      {failed}")
    print(f"Errors:      {errors}")
    print(f"Skipped:     {skipped}")
    print("----------------------------")

