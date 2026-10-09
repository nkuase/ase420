from typing import Dict, Iterator, TextIO

class SimpleDatabase:
    """Simple key-value database with control flags (before refactoring)"""
    
    def __init__(self, reader: TextIO):
        self._map: Dict[str, str] = {}
        flag = False
        
        while not flag:
            tmp = reader.readline()
            if not tmp:  # EOF
                flag = True
            else:
                tmp = tmp.strip()  # Remove newline
                flag2 = True
                s1 = []
                s2 = []
                
                for char in tmp:
                    if flag2:
                        if char == '=':
                            flag2 = False
                        else:
                            s1.append(char)
                    else:
                        s2.append(char)
                
                key = ''.join(s1)
                value = ''.join(s2)
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
