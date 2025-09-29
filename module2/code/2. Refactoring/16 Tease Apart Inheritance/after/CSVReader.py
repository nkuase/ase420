import re
from typing import Optional, List, TextIO
from io import StringIO

class CSVReader:
    """CSV reader using composition (after refactoring)"""
    
    CSV_PATTERN = re.compile(r'\s*,\s*')
    
    def __init__(self, reader: TextIO):
        self.reader = reader
        
    def read_csv(self) -> Optional[List[str]]:
        line = self.reader.readline()
        if not line:
            return None
        line = line.strip()
        return CSVReader.CSV_PATTERN.split(line)
        
    def close(self):
        self.reader.close()
