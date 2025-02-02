import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(3.5, 2.5), 6.0)

    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 3), -3)
        self.assertEqual(self.calc.subtract(3, 3), 0)
        self.assertEqual(self.calc.subtract(7.5, 2.5), 5.0)

    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(3.5, 2), 7.0)

    def test_division(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertIsNone(self.calc.divide(5, 0))  # Handling division by zero

    def test_edge_cases(self):
        """Test additional edge cases."""
        self.assertEqual(self.calc.add(1000000, 1), 1000001)
        self.assertEqual(self.calc.subtract(-1000000, -1), -999999)
        self.assertEqual(self.calc.multiply(1000000, 0), 0)
        self.assertIsNone(self.calc.divide(0, 0))  # Handling 0/0 case

if __name__ == '__main__':
    unittest.main()