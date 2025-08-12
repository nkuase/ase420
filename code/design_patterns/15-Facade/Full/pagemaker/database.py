"""
Facade Pattern - Database Subsystem Component
This class handles database operations for the page creation system.
"""

from typing import Dict


class Database:
    """
    Database utility class that loads properties from text files.
    This is part of the complex subsystem that the facade simplifies.
    """
    
    def __init__(self):
        """Private constructor - this class only has static methods."""
        pass
    
    @staticmethod
    def get_properties(dbname: str) -> Dict[str, str]:
        """
        Load properties from a database file.
        
        Args:
            dbname (str): Name of the database (without .txt extension)
            
        Returns:
            Dict[str, str]: Dictionary of key-value pairs from the file
            
        Raises:
            IOError: If the file cannot be read
        """
        filename = f"{dbname}.txt"
        properties = {}
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and '=' in line:
                        key, value = line.split('=', 1)
                        properties[key.strip()] = value.strip()
            return properties
        except IOError as e:
            raise IOError(f"Cannot read database file {filename}: {e}")
