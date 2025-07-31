import unittest
import sys
import io
from typing import List

class StandardOutputTest(unittest.TestCase):
    """Base test class for capturing and testing standard output"""
    
    def setUp(self):
        """Set up output capture"""
        self.saved_stdout = sys.stdout
        self.actual_output = io.StringIO()
        sys.stdout = self.actual_output
        
    def tearDown(self):
        """Restore original stdout"""
        sys.stdout = self.saved_stdout
        
    def get_actual_output(self) -> str:
        """Get the captured output"""
        sys.stdout.flush()
        return self.actual_output.getvalue()
        
    def get_expected_output(self, *lines: str) -> str:
        """Build expected output from lines"""
        return '\n'.join(lines) + '\n'
