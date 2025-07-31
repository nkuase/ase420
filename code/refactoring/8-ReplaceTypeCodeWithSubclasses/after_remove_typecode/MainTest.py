import unittest
from Shape import Shape
from ShapeLine import ShapeLine
from ShapeRectangle import ShapeRectangle
from ShapeOval import ShapeOval


class TestShape(unittest.TestCase):
    """Simple unit tests for Shape class"""
    
    def setUp(self):
        """Create test shapes using the same values from main()"""
        self.line = ShapeLine.create(0, 0, 100, 200)
        self.rectangle = ShapeRectangle.create(10, 20, 30, 40)
        self.oval = ShapeOval(100, 200, 300, 400)
    
    def test_shape_creation(self):
        """Test if shapes are created with correct attributes"""
        # Test line
        self.assertEqual(self.line.startx, 0)
        self.assertEqual(self.line.starty, 0)
        self.assertEqual(self.line.endx, 100)
        self.assertEqual(self.line.endy, 200)
        
        # Test rectangle
        self.assertEqual(self.rectangle.startx, 10)
        self.assertEqual(self.rectangle.starty, 20)
        self.assertEqual(self.rectangle.endx, 30)
        self.assertEqual(self.rectangle.endy, 40)
    
    def test_get_name(self):
        """Test get_name method returns correct shape names"""
        self.assertEqual(self.line.get_name(), "LINE")
        self.assertEqual(self.rectangle.get_name(), "RECTANGLE")
        self.assertEqual(self.oval.get_name(), "OVAL")
    
    def test_string_representation(self):
        """Test __str__ method"""
        line_str = str(self.line)
        rectangle_str = str(self.rectangle)
        oval_str = str(self.oval)
        
        self.assertEqual(line_str, "[ LINE, (0, 0)-(100, 200) ]")
        self.assertEqual(rectangle_str, "[ RECTANGLE, (10, 20)-(30, 40) ]")
        self.assertEqual(oval_str, "[ OVAL, (100, 200)-(300, 400) ]")
    
    def test_draw_method_exists(self):
        """Test that draw method can be called (doesn't crash)"""
        # We can't easily test print output, but we can test the method runs
        try:
            self.line.draw()
            self.rectangle.draw()
            self.oval.draw()
            # If we get here, the methods ran without error
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"draw() method failed: {e}")


if __name__ == '__main__':
    unittest.main()