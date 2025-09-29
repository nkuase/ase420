import re
from abc import ABC, abstractmethod
from typing import Optional, List
from io import StringIO

class CSVReader(ABC):
    """Abstract CSV reader (before refactoring)"""
    
    CSV_PATTERN = re.compile(r'\s*,\s*')
    
    @abstractmethod
    def read_csv(self) -> Optional[List[str]]:
        """Read next CSV line"""
        pass
        
    @abstractmethod
    def close(self):
        """Close the reader"""
        pass
