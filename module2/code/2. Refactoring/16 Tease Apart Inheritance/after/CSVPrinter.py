from abc import ABC, abstractmethod
from CSVReader import CSVReader

class CSVPrinter(ABC):
    """Abstract CSV printer using composition (after refactoring)"""
    
    def __init__(self, csv_reader: CSVReader):
        self.csv_reader = csv_reader
        
    @abstractmethod
    def print(self):
        """Print the CSV data"""
        pass
