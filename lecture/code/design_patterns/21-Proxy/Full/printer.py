"""
Proxy Pattern - Real Subject (Printer)
This class represents the real object that does the actual work.
It has expensive initialization that we want to defer.
"""

import time
from printable import Printable


class Printer(Printable):
    """
    Real subject that implements the actual printing functionality.
    This class has expensive initialization (simulated with heavy_job).
    """
    
    def __init__(self, name: str = "Unknown"):
        """
        Initialize the printer with expensive setup.
        
        Args:
            name (str): The name of the printer
        """
        self.name = name
        self._heavy_job(f"Creating Printer instance ({name})")
    
    def set_printer_name(self, name: str):
        """
        Set the printer name.
        
        Args:
            name (str): The printer name to set
        """
        self.name = name
    
    def get_printer_name(self) -> str:
        """
        Get the printer name.
        
        Returns:
            str: The current printer name
        """
        return self.name
    
    def print(self, string: str):
        """
        Print a string with the printer's name header.
        
        Args:
            string (str): The string to print
        """
        print(f"=== {self.name} ===")
        print(string)
    
    def _heavy_job(self, msg: str):
        """
        Simulate expensive initialization work.
        
        Args:
            msg (str): Message to display during the heavy work
        """
        print(msg, end='', flush=True)
        for i in range(5):
            time.sleep(0.5)  # Simulate work (reduced from 1 second for demo)
            print('.', end='', flush=True)
        print(' Completed!')
