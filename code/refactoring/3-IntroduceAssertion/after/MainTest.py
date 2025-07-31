import unittest
from SortSample import SortSample

class MainTest(unittest.TestCase):
    def test_main(self):
        sorter = SortSample([3, 1, 4, 1, 5, 9])
        sorter.sort()
        actual = str(sorter)
        expected = "[ 1, 1, 3, 4, 5, 9, ]"
        self.assertEqual(expected, actual)

    def test_zero(self):
        sorter = SortSample([])
        sorter.sort()
        actual = str(sorter)
        expected = "[ ]"
        self.assertEqual(expected, actual)

    def test_random(self):
        sorter = SortSample([8, 3, 3, 0, 0, 3, 9, 9, 7, 7])
        sorter.sort()
        actual = str(sorter)
        expected = "[ 0, 0, 3, 3, 3, 7, 7, 8, 9, 9, ]"
        print()
        print(expected)
        print(actual)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
