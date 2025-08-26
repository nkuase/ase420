from typing import List
from CSVFileReader import CSVFileReader

class CSVFileTreePrinter(CSVFileReader):
    """CSV file tree printer (before refactoring - mixed inheritance)"""
    
    def __init__(self, filename: str):
        super().__init__(filename)
        
    def print(self):
        prev_item = []
        row = 0
        
        while True:
            item = self.read_csv()
            if item is None:
                break
                
            just_print = False
            for column in range(len(item)):
                if just_print:
                    self._print_line(column, item[column])
                else:
                    if column >= len(prev_item) or item[column] != prev_item[column]:
                        self._print_line(column, item[column])
                        just_print = True
                        
            prev_item = item
            row += 1
            
    def _print_line(self, indent: int, s: str):
        print("    " * indent + s)
