import unittest
import sys
from io import StringIO
from Shape import Shape
from ShapeLine import ShapeLine
from ShapeRectangle import ShapeRectangle
from ShapeOval import ShapeOval


class TestShapeSubclass(unittest.TestCase):
    """Unit tests for Shape class with inheritance and factory methods"""
    
    def test_factory_method_creates_line(self):
        """Test factory method creates LINE shape correctly"""
        shape = Shape.create_line(10, 20, 30, 40)
        
        self.assertIsInstance(shape, ShapeLine)
        self.assertEqual(shape.get_name(), "LINE")
        self.assertEqual(shape.startx, 10)
        self.assertEqual(shape.starty, 20)
        self.assertEqual(shape.endx, 30)
        self.assertEqual(shape.endy, 40)
    
    def test_factory_method_creates_rectangle(self):
        """Test factory method creates RECTANGLE shape correctly"""
        shape = Shape.create_rectangle(5, 15, 25, 35)
        
        self.assertIsInstance(shape, ShapeRectangle)
        self.assertEqual(shape.get_name(), "RECTANGLE")
        self.assertEqual(shape.startx, 5)
        self.assertEqual(shape.starty, 15)
        self.assertEqual(shape.endx, 25)
        self.assertEqual(shape.endy, 35)
    
    def test_factory_method_creates_oval(self):
        """Test factory method creates OVAL shape correctly"""
        shape = Shape.create_oval(0, 0, 50, 60)
        
        self.assertIsInstance(shape, ShapeOval)
        self.assertEqual(shape.get_name(), "OVAL")
        self.assertEqual(shape.startx, 0)
        self.assertEqual(shape.starty, 0)
        self.assertEqual(shape.endx, 50)
        self.assertEqual(shape.endy, 60)
    
    def test_line_shape_direct_instantiation(self):
        """Test ShapeLine can be instantiated directly"""
        line = ShapeLine(1, 2, 3, 4)
        
        self.assertEqual(line.get_name(), "LINE")
        self.assertEqual(line.startx, 1)
        self.assertEqual(line.starty, 2)
        self.assertEqual(line.endx, 3)
        self.assertEqual(line.endy, 4)
    
    def test_rectangle_shape_direct_instantiation(self):
        """Test ShapeRectangle can be instantiated directly"""
        rectangle = ShapeRectangle(10, 20, 30, 40)
        
        self.assertEqual(rectangle.get_name(), "RECTANGLE")
        self.assertEqual(rectangle.startx, 10)
        self.assertEqual(rectangle.starty, 20)
        self.assertEqual(rectangle.endx, 30)
        self.assertEqual(rectangle.endy, 40)
    
    def test_oval_shape_direct_instantiation(self):
        """Test ShapeOval can be instantiated directly"""
        oval = ShapeOval(5, 10, 15, 20)
        
        self.assertEqual(oval.get_name(), "OVAL")
        self.assertEqual(oval.startx, 5)
        self.assertEqual(oval.starty, 10)
        self.assertEqual(oval.endx, 15)
        self.assertEqual(oval.endy, 20)
    
    def test_str_representation_line(self):
        """Test string representation for LINE"""
        shape = Shape.create_line(1, 2, 3, 4)
        expected = "[ LINE, (1, 2)-(3, 4) ]"
        self.assertEqual(str(shape), expected)
    
    def test_str_representation_rectangle(self):
        """Test string representation for RECTANGLE"""
        shape = Shape.create_rectangle(10, 20, 30, 40)
        expected = "[ RECTANGLE, (10, 20)-(30, 40) ]"
        self.assertEqual(str(shape), expected)
    
    def test_str_representation_oval(self):
        """Test string representation for OVAL"""
        shape = Shape.create_oval(5, 10, 15, 20)
        expected = "[ OVAL, (5, 10)-(15, 20) ]"
        self.assertEqual(str(shape), expected)
    
    def test_draw_line(self):
        """Test draw method for LINE shape"""
        shape = Shape.create_line(0, 0, 10, 10)
        
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
        shape = Shape.create_rectangle(5, 5, 15, 15)
        
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
        shape = Shape.create_oval(2, 3, 12, 13)
        
        # Capture stdout to test print output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        shape.draw()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        expected_output = "drawOval: [ OVAL, (2, 3)-(12, 13) ]\n"
        self.assertEqual(captured_output.getvalue(), expected_output)
    
    def test_polymorphism(self):
        """Test polymorphic behavior works correctly"""
        shapes = [
            Shape.create_line(0, 0, 10, 10),
            Shape.create_rectangle(5, 5, 15, 15),
            Shape.create_oval(2, 3, 12, 13)
        ]
        
        # All shapes should be drawable through base interface
        for shape in shapes:
            self.assertTrue(hasattr(shape, 'draw'))
            self.assertTrue(hasattr(shape, 'get_name'))
            # Verify each has the expected type
            name = shape.get_name()
            self.assertIn(name, ["LINE", "RECTANGLE", "OVAL"])
    
    def test_abstract_base_class(self):
        """Test that Shape cannot be instantiated directly"""
        with self.assertRaises(TypeError):
            # Shape is abstract, should not be instantiable
            shape = Shape(0, 0, 10, 10)
    
    def test_inheritance_hierarchy(self):
        """Test inheritance relationships"""
        line = ShapeLine(0, 0, 10, 10)
        rectangle = ShapeRectangle(5, 5, 15, 15)
        oval = ShapeOval(2, 3, 12, 13)
        
        # All subclasses should inherit from Shape
        self.assertIsInstance(line, Shape)
        self.assertIsInstance(rectangle, Shape)
        self.assertIsInstance(oval, Shape)


if __name__ == '__main__':
    # Run the tests
    print("Running tests for Shape class (inheritance pattern)")
    print("=" * 50)
    unittest.main(verbosity=2)
