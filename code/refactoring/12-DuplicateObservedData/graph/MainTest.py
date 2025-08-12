import unittest
import sys
from PyQt6.QtWidgets import QApplication
from IntegerDisplay import IntegerDisplay

class MainTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create QApplication instance for testing
        if not QApplication.instance():
            cls.app = QApplication(sys.argv)
        else:
            cls.app = QApplication.instance()
    
    def test_main(self):
        display = IntegerDisplay()
        display.set_value(1)
        actual = display.get_value()
        expected = 1
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
