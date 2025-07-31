"""
Print interface for Adapter Pattern Example

This interface defines the expected behavior that client code wants to use.
It represents the "Target" interface in the Adapter pattern.

In Python, we use Abstract Base Classes (ABC) to define interfaces.
"""

from abc import ABC, abstractmethod


class Print(ABC):
    """
    Abstract interface that defines the expected printing behavior.
    
    This is the "Target" interface that the client code expects to use.
    The Adapter will implement this interface and translate calls to the Adaptee.
    """
    
    @abstractmethod
    def print_weak(self) -> None:
        """
        Print text in a weak (subtle) format.
        This is the method signature that client code expects.
        """
        pass
    
    @abstractmethod
    def print_strong(self) -> None:
        """
        Print text in a strong (emphasized) format.
        This is the method signature that client code expects.
        """
        pass
