from book import Book
from book_shelf import BookShelf


def main():
    print("=== Iterator Pattern Example ===\n")
    
    book_shelf = BookShelf(4)
    book_shelf.append_book(Book("Around the World in 80 Days"))
    book_shelf.append_book(Book("Bible"))
    book_shelf.append_book(Book("Cinderella"))
    book_shelf.append_book(Book("Daddy-Long-Legs"))
    
    print(f"Created {book_shelf}\n")
    
    # Method 1: Using explicit iterator (similar to Java example)
    print("1. Using explicit iterator:")
    it = book_shelf.iterator()
    while it.has_next():
        book = it.next()
        print(f"   {book.get_name()}")
    print()
    
if __name__ == "__main__":
    main()
