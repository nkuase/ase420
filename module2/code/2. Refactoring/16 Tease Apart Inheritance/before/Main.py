from CSVStringTablePrinter import CSVStringTablePrinter
from CSVFileTreePrinter import CSVFileTreePrinter

def main():
    SAMPLE_CSV_STRING = (
        "Morning greeting,Good morning.\n"
        "Casual hello,Hello.\n"
        "Evening greeting,Good evening.\n"
        "Night farewell,Good night.\n"
    )
    
    SAMPLE_CSV_FILE = "file.csv"
    
    # Mixed inheritance example (before refactoring)
    table_printer = CSVStringTablePrinter(SAMPLE_CSV_STRING)
    table_printer.print()
    table_printer.close()
    
    tree_printer = CSVFileTreePrinter(SAMPLE_CSV_FILE)
    tree_printer.print()
    tree_printer.close()

if __name__ == "__main__":
    main()
