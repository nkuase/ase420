import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../common'))
from StandardOutputTest import StandardOutputTest
#from Label import Label
#from Person import Person
from Person_singleton import Person
from Label_singleton import Label

class MainTest(StandardOutputTest):
    def test_label(self):
        alice = Label("Alice")
        expected = '"Alice"'
        actual = str(alice)
        self.assertEqual(expected, actual)

    def test_null_label(self):
        alice = Label(None)
        expected = '"None"'
        actual = str(alice)
        self.assertEqual(expected, actual)

    def test_null_mail(self):
        alice = Person(Label("Alice"))
        expected = '[ Person: name="Alice" mail="(none)" ]'
        actual = str(alice)
        self.assertEqual(expected, actual)

    def test_to_string(self):
        alice = Person(Label("Alice"), Label("alice@example.com"))
        expected = '[ Person: name="Alice" mail="alice@example.com" ]'
        actual = str(alice)
        self.assertEqual(expected, actual)

    def test_display(self):
        alice = Person(Label("Alice"), Label("alice@example.com"))
        alice.display()
        expected = self.get_expected_output(
            "display: Alice",
            "display: alice@example.com")
        actual = self.get_actual_output()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
