from typing import Optional, List
from CSVPrinter import CSVPrinter
from CSVReader import CSVReader

class CSVTablePrinter(CSVPrinter):
    """CSV table printer using composition (after refactoring)"""
    
    def __init__(self, csv_reader: CSVReader):
        super().__init__(csv_reader)
        
    def read_csv(self) -> Optional[List[str]]:
        return self.csv_reader.read_csv()
        
    def print(self):
        print("<table>")
        row = 0
        
        while True:
            item = self.read_csv()
            if item is None:
                break
                
            print("<tr>", end="")
            for column in range(len(item)):
                print(f"<td>{item[column]}</td>", end="")
            print("</tr>")
            row += 1
            
        print("</table>")
