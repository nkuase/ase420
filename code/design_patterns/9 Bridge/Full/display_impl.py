"""
Bridge Pattern - Implementation abstraction
This abstract class defines the interface for the "implementation" side of the bridge.
It's the bridge between the abstraction and the concrete implementation.
"""

from abc import ABC, abstractmethod


class DisplayImpl(ABC):
    """
    Abstract implementation class for display operations.
    This class defines the interface that concrete implementors must follow.
    """
    
    @abstractmethod
    def raw_open(self):
        """Open the display - to be implemented by concrete classes"""
        pass
    
    @abstractmethod
    def raw_print(self):
        """Print the content - to be implemented by concrete classes"""
        pass
    
    @abstractmethod
    def raw_close(self):
        """Close the display - to be implemented by concrete classes"""
        pass
