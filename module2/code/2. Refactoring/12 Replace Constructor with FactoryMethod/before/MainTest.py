import unittest
import sys
from io import StringIO
from Shape import Shape


class TestShape(unittest.TestCase):
    """Unit tests for Shape class with direct constructor (before refactoring)"""
    
    def test_constructor_creates_line(self):
        """Test constructor creates LINE shape correctly"""
        shape = Shape(Shape.TYPECODE_LINE, 10, 20, 30, 40)
        
        self.assertEqual(shape.get_typecode(), Shape.TYPECODE_LINE)
        self.assertEqual(shape.get_name(), "LINE")
        self.assertEqual(shape.startx, 10)
        self.assertEqual(shape.starty, 20)
        self.assertEqual(shape.endx, 30)
        self.assertEqual(shape.endy, 40)
    
    def test_constructor_creates_rectangle(self):
        """Test constructor creates RECTANGLE shape correctly"""
        shape = Shape(Shape.TYPECODE_RECTANGLE, 5, 15, 25, 35)
        
        self.assertEqual(shape.get_typecode(), Shape.TYPECODE_RECTANGLE)
        self.assertEqual(shape.get_name(), "RECTANGLE")
        self.assertEqual(shape.startx, 5)
        self.assertEqual(shape.starty, 15)
        self.assertEqual(shape.endx, 25)
        self.assertEqual(shape.endy, 35)
    
    def test_constructor_creates_oval(self):
        """Test constructor creates OVAL shape correctly"""
        shape = Shape(Shape.TYPECODE_OVAL, 0, 0, 50, 60)
        
        self.assertEqual(shape.get_typecode(), Shape.TYPECODE_OVAL)
        self.assertEqual(shape.get_name(), "OVAL")
        self.assertEqual(shape.startx, 0)
        self.assertEqual(shape.starty, 0)
        self.assertEqual(shape.endx, 50)
        self.assertEqual(shape.endy, 60)
    
    def test_get_name_invalid_typecode(self):
        """Test get_name returns None for invalid typecode"""
        shape = Shape(999, 0, 0, 10, 10)  # Invalid typecode
        self.assertIsNone(shape.get_name())
    
    def test_str_representation_line(self):
        """Test string representation for LINE"""
        shape = Shape(Shape.TYPECODE_LINE, 1, 2, 3, 4)
        expected = "[ LINE, (1, 2)-(3, 4) ]"
        self.assertEqual(str(shape), expected)
    
    def test_str_representation_rectangle(self):
        """Test string representation for RECTANGLE"""
        shape = Shape(Shape.TYPECODE_RECTANGLE, 10, 20, 30, 40)
        expected = "[ RECTANGLE, (10, 20)-(30, 40) ]"
        self.assertEqual(str(shape), expected)
    
    def test_str_representation_oval(self):
        """Test string representation for OVAL"""
        shape = Shape(Shape.TYPECODE_OVAL, 5, 10, 15, 20)
        expected = "[ OVAL, (5, 10)-(15, 20) ]"
        self.assertEqual(str(shape), expected)
    
    def test_draw_line(self):
        """Test draw method for LINE shape"""
        shape = Shape(Shape.TYPECODE_LINE, 0, 0, 10, 10)
        
        # Capture stdout to test print output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        shape.draw()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        expected_output = "drawLine: [ LINE, (0, 0)-(10, 10) ]\n"
        self.assertEqual(captured_output.getvalue(), expected_output)
    
    def test_draw_rectangle(self):
        """Test draw method for RECTANGLE shape"""
        shape = Shape(Shape.TYPECODE_RECTANGLE, 5, 5, 15, 15)
        
        # Capture stdout to test print output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        shape.draw()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        expected_output = "drawRectangle: [ RECTANGLE, (5, 5)-(15, 15) ]\n"
        self.assertEqual(captured_output.getvalue(), expected_output)
    
    def test_draw_oval(self):
        """Test draw method for OVAL shape"""
        shape = Shape(Shape.TYPECODE_OVAL, 2, 3, 12, 13)
        
        # Capture stdout to test print output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        shape.draw()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        expected_output = "drawOval: [ OVAL, (2, 3)-(12, 13) ]\n"
        self.assertEqual(captured_output.getvalue(), expected_output)
    
    def test_typecode_constants(self):
        """Test that typecode constants are defined correctly"""
        self.assertEqual(Shape.TYPECODE_LINE, 0)
        self.assertEqual(Shape.TYPECODE_RECTANGLE, 1)
        self.assertEqual(Shape.TYPECODE_OVAL, 2)
    
    def test_direct_constructor_access(self):
        """Test that constructor can be called directly (before refactoring)"""
        # This test shows the problem: clients must know typecodes
        shape1 = Shape(0, 0, 0, 10, 10)  # Magic number - bad practice
        shape2 = Shape(Shape.TYPECODE_LINE, 0, 0, 10, 10)  # Better but still exposes implementation
        
        self.assertEqual(shape1.get_name(), "LINE")
        self.assertEqual(shape2.get_name(), "LINE")


if __name__ == '__main__':
    # Run the tests
    print("Running tests for Shape class (before refactoring)")
    print("=" * 50)
    unittest.main(verbosity=2)
