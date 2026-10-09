"""
Unit tests for Direction class
Tests direction creation and modification
"""
import unittest
import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Direction import Direction


class TestDirection(unittest.TestCase):
    """Test cases for Direction class"""
    
    def test_direction_creation(self):
        """Test basic direction creation"""
        direction = Direction(1, 0)
        self.assertEqual(direction.x, 1)
        self.assertEqual(direction.y, 0)
    
    def test_direction_creation_negative(self):
        """Test direction creation with negative values"""
        direction = Direction(-1, -2)
        self.assertEqual(direction.x, -1)
        self.assertEqual(direction.y, -2)
    
    def test_set_direction(self):
        """Test setting new direction values"""
        direction = Direction(1, 0)
        direction.set_direction(0, 1)
        self.assertEqual(direction.x, 0)
        self.assertEqual(direction.y, 1)
    
    def test_set_direction_multiple_times(self):
        """Test setting direction multiple times"""
        direction = Direction(0, 0)
        
        # Set first direction
        direction.set_direction(1, 2)
        self.assertEqual(direction.x, 1)
        self.assertEqual(direction.y, 2)
        
        # Change direction again
        direction.set_direction(-3, 4)
        self.assertEqual(direction.x, -3)
        self.assertEqual(direction.y, 4)
    
    def test_direction_zero(self):
        """Test direction with zero values"""
        direction = Direction(0, 0)
        self.assertEqual(direction.x, 0)
        self.assertEqual(direction.y, 0)
        
        direction.set_direction(0, 0)
        self.assertEqual(direction.x, 0)
        self.assertEqual(direction.y, 0)


if __name__ == '__main__':
    unittest.main()
