"""
Proxy Pattern - Proxy Class
This class acts as a proxy for the real Printer object.
It delays the creation of the expensive real object until actually needed.
"""

import threading
from typing import Optional
from printable import Printable
from printer import Printer


class PrinterProxy(Printable):
    """
    Proxy class that controls access to the real Printer object.
    Provides lazy initialization - the real printer is only created when needed.
    """
    
    def __init__(self, name: str = "No Name"):
        """
        Initialize the proxy with just a name (no expensive operations).
        
        Args:
            name (str): The initial name for the printer
        """
        self.name = name
        self.real: Optional[Printer] = None
        self._lock = threading.Lock()
    
    def set_printer_name(self, name: str):
        """
        Set the printer name. If the real printer exists, update it too.
        
        Args:
            name (str): The printer name to set
        """
        with self._lock:
            if self.real is not None:
                # If real printer exists, update it too
                self.real.set_printer_name(name)
            self.name = name
    
    def get_printer_name(self) -> str:
        """
        Get the printer name. This can be done without creating the real printer.
        
        Returns:
            str: The current printer name
        """
        return self.name
    
    def print(self, string: str):
        """
        Print a string. This requires the real printer, so create it if needed.
        
        Args:
            string (str): The string to print
        """
        self._realize()
        self.real.print(string)
    
    def _realize(self):
        """
        Create the real printer instance if it doesn't exist yet.
        This method implements lazy initialization with thread safety.
        """
        if self.real is None:
            with self._lock:
                # Double-check locking pattern
                if self.real is None:
                    print(f"Creating real Printer instance for '{self.name}'...")
                    self.real = Printer(self.name)
    
    def is_realized(self) -> bool:
        """
        Check if the real printer has been created.
        
        Returns:
            bool: True if the real printer exists, False otherwise
        """
        return self.real is not None
    
    def __str__(self) -> str:
        """String representation of the proxy."""
        status = "realized" if self.is_realized() else "not realized"
        return f"PrinterProxy(name='{self.name}', {status})"
