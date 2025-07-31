from typing import Dict, Iterator, TextIO

class SimpleDatabase:
    """Simple key-value database using break (after refactoring step 1)"""
    
    def __init__(self, reader: TextIO):
        self._map: Dict[str, str] = {}
        
        while True:
            line = reader.readline()
            if not line:  # EOF
                break
                
            line = line.strip()  # Remove newline
            equal_index = line.find('=')
            
            if equal_index > 0:
                key = line[:equal_index]
                value = line[equal_index + 1:]
                self._map[key] = value
    
    def put_value(self, key: str, value: str):
        """Store a key-value pair"""
        self._map[key] = value
        
    def get_value(self, key: str) -> str:
        """Get value by key"""
        return self._map.get(key, "")
        
    def iterator(self) -> Iterator[str]:
        """Get iterator over keys"""
        return iter(self._map.keys())
