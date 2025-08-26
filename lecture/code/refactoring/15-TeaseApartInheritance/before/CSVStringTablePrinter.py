from CSVStringReader import CSVStringReader

class CSVStringTablePrinter(CSVStringReader):
    """CSV string table printer (before refactoring - mixed inheritance)"""
    
    def __init__(self, string: str):
        super().__init__(string)
        
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
