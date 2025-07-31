"""
Print abstract class for Adapter Pattern Example (Sample2)

This abstract class defines the expected behavior that client code wants to use.
It represents the "Target" class in the Adapter pattern.

Unlike Sample1 which uses an interface, this version uses an abstract class
to demonstrate a different approach to the Adapter pattern.
"""

from abc import ABC, abstractmethod


class Print(ABC):
    """
    Abstract class that defines the expected printing behavior.
    
    This is the "Target" class that the client code expects to use.
    The Adapter will extend this class and implement its abstract methods.
    
    This version uses abstract class inheritance rather than interface implementation.
    """
    
    @abstractmethod
    def print_weak(self) -> None:
        """
        Print text in a weak (subtle) format.
        This is the abstract method that subclasses must implement.
        """
        pass
    
    @abstractmethod
    def print_strong(self) -> None:
        """
        Print text in a strong (emphasized) format.
        This is the abstract method that subclasses must implement.
        """
        pass
    
    def describe_functionality(self) -> None:
        """
        Concrete method available to all subclasses.
        Demonstrates that abstract classes can have concrete methods.
        """
        print("This Print class provides weak and strong formatting options.")
