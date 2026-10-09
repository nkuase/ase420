"""
Unit tests for Command class
Tests the command parsing and predefined command constants
"""
import unittest
import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Command import Command


class TestCommand(unittest.TestCase):
    """Test cases for Command class"""
    
    def test_command_creation(self):
        """Test basic command creation"""
        cmd = Command("test")
        self.assertEqual(cmd.get_name(), "test")
    
    def test_predefined_commands(self):
        """Test that all predefined commands exist and have correct names"""
        self.assertEqual(Command.FORWARD.get_name(), "forward")
        self.assertEqual(Command.BACKWARD.get_name(), "backward") 
        self.assertEqual(Command.TURN_RIGHT.get_name(), "right")
        self.assertEqual(Command.TURN_LEFT.get_name(), "left")
    
    def test_parse_valid_commands(self):
        """Test parsing valid command strings"""
        self.assertEqual(Command.parse_command("forward"), Command.FORWARD)
        self.assertEqual(Command.parse_command("backward"), Command.BACKWARD)
        self.assertEqual(Command.parse_command("right"), Command.TURN_RIGHT)
        self.assertEqual(Command.parse_command("left"), Command.TURN_LEFT)
    
    def test_parse_invalid_command(self):
        """Test parsing invalid command returns None"""
        self.assertIsNone(Command.parse_command("invalid"))
        self.assertIsNone(Command.parse_command(""))
        self.assertIsNone(Command.parse_command("FORWARD"))  # Case sensitive
    
    def test_command_identity(self):
        """Test that parsed commands are identical to constants"""
        # Same command should be the exact same object
        self.assertIs(Command.parse_command("forward"), Command.FORWARD)
        self.assertIs(Command.parse_command("left"), Command.TURN_LEFT)


if __name__ == '__main__':
    unittest.main()
