from Database import Database
from typing import Iterator, Optional

class AddressFile:
    """Address file with hidden database (after refactoring)"""
    
    def __init__(self, filename: str):
        self._database = Database(filename)  # Private - hidden delegate
        
    def names(self) -> Iterator[str]:
        """Get all names in the address file"""
        return iter(self._database.get_properties().keys())
        
    def set(self, key: str, value: str):
        """Delegation method - hides database"""
        self._database.set(key, value)
        
    def get(self, key: str) -> Optional[str]:
        """Delegation method - hides database"""
        return self._database.get(key)
        
    def update(self):
        """Delegation method - hides database"""
        self._database.update()
