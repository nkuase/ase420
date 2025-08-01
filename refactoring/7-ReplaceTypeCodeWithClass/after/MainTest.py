import unittest
from ItemType import ItemType
from Item import Item


class TestItem(unittest.TestCase):
    """Simple test cases for the Item class"""
    
    def test_create_book(self):
        """Test creating a book item"""
        book = Item(ItemType.BOOK, "Python Programming", 1500)
        
        self.assertEqual(book.get_typecode(), 0)
        self.assertEqual(book.get_title(), "Python Programming")
        self.assertEqual(book.get_price(), 1500)
    
    def test_create_dvd(self):
        """Test creating a DVD item"""
        dvd = Item(ItemType.DVD, "The Matrix", 2000)
        
        self.assertEqual(dvd.get_typecode(), 1)
        self.assertEqual(dvd.get_title(), "The Matrix")
        self.assertEqual(dvd.get_price(), 2000)
    
    def test_create_software(self):
        """Test creating a software item"""
        software = Item(ItemType.SOFTWARE, "Adobe Photoshop", 50000)
        
        self.assertEqual(software.get_typecode(), 2)
        self.assertEqual(software.get_title(), "Adobe Photoshop")
        self.assertEqual(software.get_price(), 50000)
    
    def test_str_method(self):
        """Test the string representation"""
        item = Item(ItemType.BOOK, "Clean Code", 3000)
        expected = "[ 0, Clean Code, 3000 ]"
        
        self.assertEqual(str(item), expected)
    
    def test_type_constants(self):
        """Test that type code constants are correct"""
        self.assertEqual(ItemType.BOOK.get_typecode(), 0)
        self.assertEqual(ItemType.DVD.get_typecode(), 1)
        self.assertEqual(ItemType.SOFTWARE.get_typecode(), 2)


if __name__ == '__main__':
    unittest.main()