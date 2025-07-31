"""
Main module for Iterator Pattern Example

This demonstrates the Iterator pattern in Python, showing how to:
1. Create a collection that supports iteration
2. Use explicit iterator methods
3. Use Python's built-in iteration (for loops)

The Iterator pattern provides a way to access elements of a collection
sequentially without exposing the underlying representation.
"""

from book import Book
from book_shelf import BookShelf


def main():
    """Demonstrate the Iterator pattern with different iteration methods."""
    
    print("=== Iterator Pattern Example ===\n")
    
    # Create a BookShelf with capacity for 4 books
    book_shelf = BookShelf(4)
    
    # Add books to the shelf
    book_shelf.append_book(Book("Around the World in 80 Days"))
    book_shelf.append_book(Book("Bible"))
    book_shelf.append_book(Book("Cinderella"))
    book_shelf.append_book(Book("Daddy-Long-Legs"))
    
    print(f"Created {book_shelf}\n")
    
    # Method 1: Using explicit iterator (similar to Java example)
    print("1. Using explicit iterator:")
    it = book_shelf.iterator()
    while it.has_next():
        book = next(it)
        print(f"   {book.get_name()}")
    print()
    
    # Method 2: Using Python's built-in iteration (enhanced for loop equivalent)
    print("2. Using Python's for loop (Pythonic way):")
    for book in book_shelf:
        print(f"   {book.get_name()}")
    print()
    
    # Method 3: Using Python's iterator protocol directly
    print("3. Using Python's iterator protocol directly:")
    iterator = iter(book_shelf)
    try:
        while True:
            book = next(iterator)
            print(f"   {book.get_name()}")
    except StopIteration:
        pass  # Normal end of iteration
    print()
    
    # Demonstrate the pattern's benefits
    print("4. Benefits of Iterator Pattern:")
    print(f"   - Total books: {len(book_shelf)}")
    print(f"   - Can iterate without knowing internal structure")
    print(f"   - Multiple iterators can be used simultaneously")
    
    # Example with multiple iterators
    print("\n5. Multiple iterators example:")
    iter1 = book_shelf.iterator()
    iter2 = book_shelf.iterator()
    
    if iter1.has_next() and iter2.has_next():
        print(f"   Iterator 1 first book: {next(iter1).get_name()}")
        print(f"   Iterator 2 first book: {next(iter2).get_name()}")
        print("   Both iterators work independently!")


if __name__ == "__main__":
    main()
