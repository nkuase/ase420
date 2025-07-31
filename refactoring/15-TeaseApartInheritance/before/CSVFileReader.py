from typing import Optional, List
from CSVReader import CSVReader

class CSVFileReader(CSVReader):
    """CSV file reader (before refactoring)"""
    
    def __init__(self, filename: str):
        self.file = open(filename, 'r')
        
    def read_csv(self) -> Optional[List[str]]:
        line = self.file.readline()
        if not line:
            return None
        line = line.strip()
        return CSVReader.CSV_PATTERN.split(line)
        
    def close(self):
        self.file.close()
