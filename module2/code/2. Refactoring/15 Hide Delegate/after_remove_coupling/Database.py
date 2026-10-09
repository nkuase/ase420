import os
from typing import Dict, Optional, Iterator

class Database:
    """Simple key-value database with keys() method"""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.properties: Dict[str, str] = {}
        self.load()
        
    def load(self):
        """Load properties from file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            if '=' in line:
                                key, value = line.split('=', 1)
                                # Handle escaped spaces
                                key = key.replace('\\ ', ' ')
                                self.properties[key] = value
            except IOError:
                pass
                
    def set(self, key: str, value: str):
        """Set a key-value pair"""
        self.properties[key] = value
        
    def get(self, key: str) -> Optional[str]:
        """Get value by key"""
        return self.properties.get(key)
        
    def update(self):
        """Save properties to file"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write("#\n")
            for key, value in self.properties.items():
                # Escape spaces in keys
                escaped_key = key.replace(' ', '\\ ')
                f.write(f"{escaped_key}={value}\n")
                
    def keys(self) -> Iterator[str]:
        """Get iterator over keys - alternative to getProperties().propertyNames()"""
        return iter(self.properties.keys())
