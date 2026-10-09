import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '../../common'))

from StandardOutputTest import StandardOutputTest
from Main import main

class MainTest(StandardOutputTest):
    def test_main(self):
        main()
        
        expected = self.get_expected_output(
            "name=Hiroshi Yuki, mail=hyuki@example.com",
            "name=Tomura, mail=tomura@example.com", 
            "name=Hanako Sato, mail=hanako@example.com")
        actual = self.get_actual_output()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
