import unittest
from FindInt import FindInt

class MainTest(unittest.TestCase):
    def test_found(self):
        data = [1, 9, 0, 2, 8, 5, 6, 3, 4, 7]
        actual = FindInt.find(data, 5)
        expected = True
        self.assertEqual(expected, actual)
        
    def test_not_found(self):
        data = [1, 9, 0, 2, 8, 5, 6, 3, 4, 7]
        actual = FindInt.find(data, 10)
        expected = False
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
