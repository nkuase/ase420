"""
Unit tests for Position class (Exception version)
Tests position creation and relative movement - unchanged from before version
"""
import unittest
import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Position import Position


class TestPosition(unittest.TestCase):
    """Test cases for Position class"""
    
    def test_position_creation(self):
        """Test basic position creation"""
        position = Position(5, 10)
        self.assertEqual(position.x, 5)
        self.assertEqual(position.y, 10)
    
    def test_position_creation_zero(self):
        """Test position creation at origin"""
        position = Position(0, 0)
        self.assertEqual(position.x, 0)
        self.assertEqual(position.y, 0)
    
    def test_position_creation_negative(self):
        """Test position creation with negative coordinates"""
        position = Position(-3, -7)
        self.assertEqual(position.x, -3)
        self.assertEqual(position.y, -7)
    
    def test_relative_move_positive(self):
        """Test relative movement with positive deltas"""
        position = Position(1, 2)
        position.relative_move(3, 4)
        self.assertEqual(position.x, 4)  # 1 + 3
        self.assertEqual(position.y, 6)  # 2 + 4
    
    def test_relative_move_negative(self):
        """Test relative movement with negative deltas"""
        position = Position(10, 20)
        position.relative_move(-5, -8)
        self.assertEqual(position.x, 5)   # 10 - 5
        self.assertEqual(position.y, 12)  # 20 - 8
    
    def test_relative_move_zero(self):
        """Test relative movement with zero deltas (no movement)"""
        position = Position(7, 3)
        position.relative_move(0, 0)
        self.assertEqual(position.x, 7)
        self.assertEqual(position.y, 3)
    
    def test_multiple_relative_moves(self):
        """Test multiple relative movements"""
        position = Position(0, 0)
        
        # First move
        position.relative_move(1, 2)
        self.assertEqual(position.x, 1)
        self.assertEqual(position.y, 2)
        
        # Second move
        position.relative_move(-2, 3)
        self.assertEqual(position.x, -1)  # 1 - 2
        self.assertEqual(position.y, 5)   # 2 + 3
        
        # Third move
        position.relative_move(4, -1)
        self.assertEqual(position.x, 3)   # -1 + 4
        self.assertEqual(position.y, 4)   # 5 - 1


if __name__ == '__main__':
    unittest.main()
