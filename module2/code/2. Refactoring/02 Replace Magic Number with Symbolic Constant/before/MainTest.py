import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../common'))

from StandardOutputTest import StandardOutputTest
from Main import main

class MainTest(StandardOutputTest):
    def test_main(self):
        # Expected
        expected = self.get_expected_output(
            "Andrew walks.",
            "Andrew stops.",
            "Andrew jumps.")

        # Actual
        main()
        actual = self.get_actual_output()

        # Assert
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
