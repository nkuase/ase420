from CSVTablePrinter import CSVTablePrinter
from CSVTreePrinter import CSVTreePrinter
from CSVStringReader import CSVStringReader
from CSVFileReader import CSVFileReader

def main():
    SAMPLE_CSV_STRING = (
        "Morning greeting,Good morning.\n"
        "Casual hello,Hello.\n"
        "Evening greeting,Good evening.\n"
        "Night farewell,Good night.\n"
    )
    
    SAMPLE_CSV_FILE = "file.csv"
    
    # Composition example (after refactoring)
    string_reader = CSVStringReader(SAMPLE_CSV_STRING)
    table_printer = CSVTablePrinter(string_reader)
    table_printer.print()
    string_reader.close()
    
    file_reader = CSVFileReader(SAMPLE_CSV_FILE)
    tree_printer = CSVTreePrinter(file_reader)
    tree_printer.print()
    file_reader.close()

if __name__ == "__main__":
    main()
