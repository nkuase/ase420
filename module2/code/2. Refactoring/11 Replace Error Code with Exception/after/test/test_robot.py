"""
Unit tests for Robot class (Exception version)
Tests robot creation, command execution, movement, and exception handling
"""
import unittest
import sys
import os
from io import StringIO

# Add parent directory to path to import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Robot import Robot
from Position import Position
from Direction import Direction
from Command import Command
from InvalidCommandException import InvalidCommandException


class TestRobot(unittest.TestCase):
    """Test cases for Robot class using exceptions"""
    
    def test_robot_creation(self):
        """Test basic robot creation"""
        robot = Robot("TestBot")
        self.assertEqual(robot.name, "TestBot")
        self.assertEqual(robot.position.x, 0)
        self.assertEqual(robot.position.y, 0)
        self.assertEqual(robot.direction.x, 0)
        self.assertEqual(robot.direction.y, 1)  # Initially facing north
    
    def test_robot_str_representation(self):
        """Test robot string representation"""
        robot = Robot("R2D2")
        expected = "[ Robot: R2D2 position(0, 0), direction(0, 1) ]"
        self.assertEqual(str(robot), expected)
    
    def test_execute_command_forward(self):
        """Test forward command execution (no exception means success)"""
        robot = Robot("TestBot")
        # Should not raise an exception
        robot.execute_command("forward")
        self.assertEqual(robot.position.x, 0)
        self.assertEqual(robot.position.y, 1)  # Moved forward in y direction
    
    def test_execute_command_backward(self):
        """Test backward command execution (no exception means success)"""
        robot = Robot("TestBot")
        # Should not raise an exception
        robot.execute_command("backward")
        self.assertEqual(robot.position.x, 0)
        self.assertEqual(robot.position.y, -1)  # Moved backward in y direction
    
    def test_execute_command_turn_right(self):
        """Test right turn command execution (no exception means success)"""
        robot = Robot("TestBot")
        # Should not raise an exception
        robot.execute_command("right")
        self.assertEqual(robot.direction.x, 1)   # Now facing east
        self.assertEqual(robot.direction.y, 0)
        # Position should not change
        self.assertEqual(robot.position.x, 0)
        self.assertEqual(robot.position.y, 0)
    
    def test_execute_command_turn_left(self):
        """Test left turn command execution (no exception means success)"""
        robot = Robot("TestBot")
        # Should not raise an exception
        robot.execute_command("left")
        self.assertEqual(robot.direction.x, -1)  # Now facing west
        self.assertEqual(robot.direction.y, 0)
        # Position should not change
        self.assertEqual(robot.position.x, 0)
        self.assertEqual(robot.position.y, 0)
    
    def test_execute_command_invalid_throws_exception(self):
        """Test invalid command execution throws InvalidCommandException"""
        robot = Robot("TestBot")
        
        with self.assertRaises(InvalidCommandException) as context:
            robot.execute_command("invalid")
        
        self.assertEqual(context.exception.message, "invalid")
        
        # Robot state should not change
        self.assertEqual(robot.position.x, 0)
        self.assertEqual(robot.position.y, 0)
        self.assertEqual(robot.direction.x, 0)
        self.assertEqual(robot.direction.y, 1)
    
    def test_multiple_invalid_commands_throw_exceptions(self):
        """Test that various invalid commands all throw exceptions"""
        robot = Robot("TestBot")
        invalid_commands = ["invalid", "jump", "FORWARD", "123", ""]
        
        for cmd in invalid_commands:
            with self.assertRaises(InvalidCommandException) as context:
                robot.execute_command(cmd)
            self.assertEqual(context.exception.message, cmd)
    
    def test_full_rotation(self):
        """Test full 360-degree rotation using exceptions"""
        robot = Robot("TestBot")
        
        # Start facing north (0, 1)
        self.assertEqual(robot.direction.x, 0)
        self.assertEqual(robot.direction.y, 1)
        
        # Turn right to face east (1, 0)
        robot.execute_command("right")
        self.assertEqual(robot.direction.x, 1)
        self.assertEqual(robot.direction.y, 0)
        
        # Turn right to face south (0, -1)
        robot.execute_command("right")
        self.assertEqual(robot.direction.x, 0)
        self.assertEqual(robot.direction.y, -1)
        
        # Turn right to face west (-1, 0)
        robot.execute_command("right")
        self.assertEqual(robot.direction.x, -1)
        self.assertEqual(robot.direction.y, 0)
        
        # Turn right to face north again (0, 1)
        robot.execute_command("right")
        self.assertEqual(robot.direction.x, 0)
        self.assertEqual(robot.direction.y, 1)
    
    def test_movement_after_turning(self):
        """Test movement after changing direction"""
        robot = Robot("TestBot")
        
        # Turn right to face east
        robot.execute_command("right")
        
        # Move forward (should move in x direction)
        robot.execute_command("forward")
        self.assertEqual(robot.position.x, 1)
        self.assertEqual(robot.position.y, 0)
        
        # Move backward (should move back in x direction)
        robot.execute_command("backward")
        self.assertEqual(robot.position.x, 0)
        self.assertEqual(robot.position.y, 0)
    
    def test_execute_sequence_valid(self):
        """Test executing a sequence of valid commands"""
        robot = Robot("TestBot")
        
        # Capture stdout to test that no error messages are printed
        original_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()
        
        try:
            robot.execute("forward right forward")
            
            # Check final position and direction
            self.assertEqual(robot.position.x, 1)
            self.assertEqual(robot.position.y, 1)
            self.assertEqual(robot.direction.x, 1)  # Facing east
            self.assertEqual(robot.direction.y, 0)
            
            # Should not print any error messages
            output = captured_output.getvalue()
            self.assertEqual(output, "")
            
        finally:
            sys.stdout = original_stdout
    
    def test_execute_sequence_with_invalid(self):
        """Test executing a sequence with invalid command"""
        robot = Robot("TestBot")
        
        # Capture stdout to test print output
        original_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()
        
        try:
            robot.execute("forward invalid right")
            
            # Should stop at invalid command
            self.assertEqual(robot.position.x, 0)
            self.assertEqual(robot.position.y, 1)   # Only moved forward once
            self.assertEqual(robot.direction.x, 0)  # Still facing north (didn't turn)
            self.assertEqual(robot.direction.y, 1)
            
            # Should print error message
            output = captured_output.getvalue().strip()
            self.assertEqual(output, "Invalid command: invalid")
            
        finally:
            sys.stdout = original_stdout
    
    def test_execute_sequence_stops_on_first_invalid(self):
        """Test that execution stops on first invalid command in sequence"""
        robot = Robot("TestBot")
        
        # Capture stdout to test print output
        original_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()
        
        try:
            robot.execute("forward bad_command right left backward")
            
            # Should execute only "forward" then stop
            self.assertEqual(robot.position.x, 0)
            self.assertEqual(robot.position.y, 1)   # Only forward executed
            self.assertEqual(robot.direction.x, 0)  # No turns executed
            self.assertEqual(robot.direction.y, 1)
            
            # Should print error for the bad command
            output = captured_output.getvalue().strip()
            self.assertEqual(output, "Invalid command: bad_command")
            
        finally:
            sys.stdout = original_stdout
    
    def test_empty_command_sequence(self):
        """Test executing empty command sequence"""
        robot = Robot("TestBot")
        
        # Should not raise exception
        robot.execute("")
        
        # Robot state should not change
        self.assertEqual(robot.position.x, 0)
        self.assertEqual(robot.position.y, 0)
        self.assertEqual(robot.direction.x, 0)
        self.assertEqual(robot.direction.y, 1)
    
    def test_whitespace_only_sequence(self):
        """Test executing sequence with only whitespace"""
        robot = Robot("TestBot")
        
        # Should not raise exception
        robot.execute("   ")
        
        # Robot state should not change
        self.assertEqual(robot.position.x, 0)
        self.assertEqual(robot.position.y, 0)
        self.assertEqual(robot.direction.x, 0)
        self.assertEqual(robot.direction.y, 1)


if __name__ == '__main__':
    unittest.main()
