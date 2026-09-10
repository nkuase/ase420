import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def test_get_full_name(self):
        e = Employee("Doe", "John", 50000)
        self.assertEqual(e.get_full_name(), "Doe,John")

    def test_raise_salary(self):
        e = Employee("Smith", "Jane", 2000)
        e.raise_salary(1.1)
        self.assertAlmostEqual(e.salary, 2200.0)

    def test_zero_raise(self):
        e = Employee("Jones", "Bob", 3000)
        e.raise_salary(1.0)
        self.assertEqual(e.salary, 3000)
