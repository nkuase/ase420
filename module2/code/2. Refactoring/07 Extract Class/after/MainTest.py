import unittest
from Book import Book

class MainTest(unittest.TestCase):
    def test_main(self):
        book = Book(
            "The title of the book",
            "ISBNxxxx",
            "$12.34",
            "A. U. Thor",
            "author@example.com")
        actual = book.to_xml()
        expected = ("<book>"
                   "<title>The title of the book</title>"
                   "<isbn>ISBNxxxx</isbn>"
                   "<price>$12.34</price>"
                   "<author>"
                   "<name>A. U. Thor</name>"
                   "<mail>author@example.com</mail>"
                   "</author>"
                   "</book>")
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
