import unittest
from Shape import Shape


class TestShape(unittest.TestCase):
    """Simple unit tests for Shape class"""
    
    def setUp(self):
        """Create test shapes using the same values from main()"""
        self.line = Shape(Shape.TYPECODE_LINE, 0, 0, 100, 200)
        self.rectangle = Shape(Shape.TYPECODE_RECTANGLE, 10, 20, 30, 40)
        self.oval = Shape(Shape.TYPECODE_OVAL, 100, 200, 300, 400)
    
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
    
    def test_get_typecode(self):
        """Test get_typecode method"""
        self.assertEqual(self.line.get_typecode(), 0)
        self.assertEqual(self.rectangle.get_typecode(), 1)
        self.assertEqual(self.oval.get_typecode(), 2)
    
    def test_get_name(self):
        """Test get_name method returns correct shape names"""
        self.assertEqual(self.line.get_name(), "LINE")
        self.assertEqual(self.rectangle.get_name(), "RECTANGLE")
        self.assertEqual(self.oval.get_name(), "OVAL")
    
    def test_get_name_invalid(self):
        """Test get_name with invalid typecode"""
        invalid_shape = Shape(999, 0, 0, 10, 10)
        self.assertIsNone(invalid_shape.get_name())
    
    def test_string_representation(self):
        """Test __str__ method"""
        line_str = str(self.line)
        rectangle_str = str(self.rectangle)
        oval_str = str(self.oval)
        
        self.assertEqual(line_str, "[ LINE, (0, 0)-(100, 200) ]")
        self.assertEqual(rectangle_str, "[ RECTANGLE, (10, 20)-(30, 40) ]")
        self.assertEqual(oval_str, "[ OVAL, (100, 200)-(300, 400) ]")
    
    def test_type_constants(self):
        """Test class constants have correct values"""
        self.assertEqual(Shape.TYPECODE_LINE, 0)
        self.assertEqual(Shape.TYPECODE_RECTANGLE, 1)
        self.assertEqual(Shape.TYPECODE_OVAL, 2)
    
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