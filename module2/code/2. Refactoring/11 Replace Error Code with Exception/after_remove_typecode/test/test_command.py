"""
Unit tests for Command class (Exception version)
Tests the command parsing and predefined command constants with exception handling
"""
import unittest
import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Command import Command, Forward, Backward, Left, Right
from InvalidCommandException import InvalidCommandException


class TestCommand(unittest.TestCase):
    """Test cases for Command class using exceptions"""
    
    def test_command_creation(self):
        """Test basic command creation"""
        cmd = Command("test")
        self.assertEqual(cmd.get_name(), "test")
    
    def test_predefined_commands(self):
        """Test that all predefined commands exist and have correct names"""
        self.assertEqual(Forward().get_name(), "forward")
        self.assertEqual(Backward().get_name(), "backward") 
        self.assertEqual(Right().get_name(), "right")
        self.assertEqual(Left().get_name(), "left")
    
    def test_parse_invalid_command_throws_exception(self):
        """Test parsing invalid command throws InvalidCommandException"""
        with self.assertRaises(InvalidCommandException) as context:
            Command.parse_command("invalid")
        self.assertEqual(context.exception.message, "invalid")
        
        with self.assertRaises(InvalidCommandException) as context:
            Command.parse_command("")
        self.assertEqual(context.exception.message, "")
        
        with self.assertRaises(InvalidCommandException) as context:
            Command.parse_command("FORWARD")  # Case sensitive
        self.assertEqual(context.exception.message, "FORWARD")
    
    def test_command_type_identity(self):
        """Test that parsed commands are identical to constants"""
        self.assertEqual(type(Command.parse_command("forward")), Forward)
        self.assertEqual(type(Command.parse_command("left")), Left)
    
    def test_invalid_command_exception_details(self):
        """Test InvalidCommandException contains proper error details"""
        test_cases = ["invalid", "xyz", "123", "TURN"]
        
        for invalid_cmd in test_cases:
            with self.assertRaises(InvalidCommandException) as context:
                Command.parse_command(invalid_cmd)
            
            # Check that exception message matches the invalid command
            self.assertEqual(context.exception.message, invalid_cmd)


if __name__ == '__main__':
    unittest.main()
