from Book import Book

def main():
    refactoring = Book(
        "Refactoring: improving the design of existing code",
        "ISBN0201485672",
        "$44.95",
        "Martin Fowler",
        "fowler@acm.org")

    math = Book(
        "Mathematics for Programmers",
        "ISBN4797329734",
        "$20.00",
        "Hiroshi Yuki",
        "hyuki@hyuki.com")

    print("refactoring:")
    print(refactoring.to_xml())

    print("math:")
    print(math.to_xml())

if __name__ == "__main__":
    main()
