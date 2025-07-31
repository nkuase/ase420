from Database import Database
from typing import Iterator, Optional

class AddressFile:
    """Address file using Database.keys() method (again version)"""
    
    def __init__(self, filename: str):
        self._database = Database(filename)  # Private - hidden delegate
        
    def names(self) -> Iterator[str]:
        """Get all names using Database.keys() method"""
        return self._database.keys()
        
    def set(self, key: str, value: str):
        """Delegation method - hides database"""
        self._database.set(key, value)
        
    def get(self, key: str) -> Optional[str]:
        """Delegation method - hides database"""
        return self._database.get(key)
        
    def update(self):
        """Delegation method - hides database"""
        self._database.update()
