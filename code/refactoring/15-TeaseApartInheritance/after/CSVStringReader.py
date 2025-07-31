from io import StringIO
from CSVReader import CSVReader

class CSVStringReader(CSVReader):
    """CSV string reader factory (after refactoring)"""
    
    def __init__(self, string: str):
        string_io = StringIO(string)
        super().__init__(string_io)
