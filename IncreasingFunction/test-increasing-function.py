import unittest
from IncreasingFunction import f, find 

class TestFunctions(unittest.TestCase):
    def test_f(self):
        # Test case 1: n is 0
        result = f(0)
        self.assertEqual(result, 0.0, "Test case 1 failed: Expected 0.0")

        # Test case 2: n is a positive integer
        result = f(3)
        self.assertIsInstance(result, float, "Test case 2 failed: Expected a float")

    def test_find(self):
        # Test case 1: Value in the range
        y = f(3)
        result = find(f, y, 0, 10000000000)
        self.assertEqual(result, 3, "Test case 1 failed: Expected 3")

        # Test case 2: Value not in the range
        z = y + 1e-8
        result = find(f, z, 0, 10000000000)
        self.assertEqual(result, -1, "Test case 2 failed: Expected -1")

        # Test case 3: Lower bound of the range
        result = find(f, y, 3, 10000000000)
        self.assertEqual(result, 3, "Test case 3 failed: Expected 3")

        # Test case 4: Upper bound of the range
        result = find(f, y, 0, 3)
        self.assertEqual(result, 3, "Test case 4 failed: Expected 3")

if __name__ == '__main__':
    unittest.main()