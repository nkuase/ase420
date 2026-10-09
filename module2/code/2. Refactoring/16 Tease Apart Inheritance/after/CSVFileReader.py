from CSVReader import CSVReader

class CSVFileReader(CSVReader):
    """CSV file reader factory (after refactoring)"""
    
    def __init__(self, filename: str):
        file_handle = open(filename, 'r')
        super().__init__(file_handle)
