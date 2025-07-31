"""
Flyweight Pattern - BigCharFactory (Flyweight Factory)
This class manages and provides shared BigChar flyweight instances.
Ensures that flyweights are shared properly to save memory.
"""

import threading
from typing import Dict
from big_char import BigChar


class BigCharFactory:
    """
    Flyweight factory that manages the creation and sharing of BigChar instances.
    Implements the Singleton pattern to ensure only one factory exists.
    """
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        """Implement thread-safe singleton pattern."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._pool: Dict[str, BigChar] = {}
        return cls._instance
    
    @classmethod
    def get_instance(cls) -> 'BigCharFactory':
        """
        Get the singleton instance of the factory.
        
        Returns:
            BigCharFactory: The singleton factory instance
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def get_big_char(self, charname: str) -> BigChar:
        """
        Get a BigChar flyweight instance for the specified character.
        Creates new instances only if they don't already exist in the pool.
        
        Args:
            charname (str): The character to get (e.g., '0', '1', '-')
            
        Returns:
            BigChar: A shared BigChar instance
        """
        with self._lock:
            if charname not in self._pool:
                # Create new BigChar only if it doesn't exist
                print(f"Creating new BigChar for '{charname}'")
                self._pool[charname] = BigChar(charname)
            else:
                print(f"Reusing existing BigChar for '{charname}'")
            
            return self._pool[charname]
    
    def get_pool_size(self) -> int:
        """
        Get the number of flyweight instances in the pool.
        
        Returns:
            int: Number of cached BigChar instances
        """
        return len(self._pool)
    
    def get_cached_characters(self) -> list:
        """
        Get list of characters that are cached in the pool.
        
        Returns:
            list: List of cached character names
        """
        return list(self._pool.keys())
    
    def clear_pool(self):
        """Clear the flyweight pool (for testing purposes)."""
        with self._lock:
            self._pool.clear()
            print("Flyweight pool cleared")
