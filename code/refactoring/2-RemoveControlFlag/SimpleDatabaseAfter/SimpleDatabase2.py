from typing import Dict, Iterator, TextIO
import re

class SimpleDatabase:
    """Simple key-value database using regex (after refactoring step 2)"""
    
    def __init__(self, reader: TextIO):
        self._map: Dict[str, str] = {}
        self._pattern = re.compile(r'([^=]+)=(.*)')
        
        while True:
            line = reader.readline()
            if not line:  # EOF
                break
                
            line = line.strip()  # Remove newline
            match = self._pattern.match(line)
            
            if match:
                key = match.group(1)
                value = match.group(2)
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
