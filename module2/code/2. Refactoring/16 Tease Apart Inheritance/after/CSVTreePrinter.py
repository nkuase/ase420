from typing import Optional, List
from CSVPrinter import CSVPrinter
from CSVReader import CSVReader

class CSVTreePrinter(CSVPrinter):
    """CSV tree printer using composition (after refactoring)"""
    
    def __init__(self, csv_reader: CSVReader):
        super().__init__(csv_reader)
        
    def read_csv(self) -> Optional[List[str]]:
        return self.csv_reader.read_csv()
        
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
