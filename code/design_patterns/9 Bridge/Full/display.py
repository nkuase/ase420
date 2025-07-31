"""
Bridge Pattern - Abstraction class
This class represents the "abstraction" side of the bridge pattern.
It uses a DisplayImpl object to perform the actual display operations.
"""

from display_impl import DisplayImpl


class Display:
    """
    The abstraction class that uses an implementation object.
    This class defines the interface that clients use.
    It delegates the actual work to the DisplayImpl object.
    """
    
    def __init__(self, impl: DisplayImpl):
        """
        Initialize with a concrete implementation.
        
        Args:
            impl (DisplayImpl): The implementation object to use
        """
        self.impl = impl
    
    def open(self):
        """Open the display using the implementation"""
        self.impl.raw_open()
    
    def print(self):
        """Print the content using the implementation"""
        self.impl.raw_print()
    
    def close(self):
        """Close the display using the implementation"""
        self.impl.raw_close()
    
    def display(self):
        """
        Template method that defines the display sequence.
        This method is final (not intended to be overridden).
        """
        self.open()
        self.print()
        self.close()
