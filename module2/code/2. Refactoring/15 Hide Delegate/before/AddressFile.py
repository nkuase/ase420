from Database import Database
from typing import Iterator

class AddressFile:
    """Address file with exposed database (before refactoring)"""
    
    def __init__(self, filename: str):
        self.database = Database(filename)
        
    def get_database(self) -> Database:
        """Exposes internal database - this will be removed in refactoring"""
        return self.database
        
    def names(self) -> Iterator[str]:
        """Get all names in the address file"""
        return iter(self.database.get_properties().keys())
