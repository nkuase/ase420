from typing import Optional, List
from io import StringIO
from CSVReader import CSVReader

class CSVStringReader(CSVReader):
    """CSV string reader (before refactoring)"""
    
    def __init__(self, string: str):
        self.string_io = StringIO(string)
        
    def read_csv(self) -> Optional[List[str]]:
        line = self.string_io.readline()
        if not line:
            return None
        line = line.strip()
        return CSVReader.CSV_PATTERN.split(line)
        
    def close(self):
        self.string_io.close()
