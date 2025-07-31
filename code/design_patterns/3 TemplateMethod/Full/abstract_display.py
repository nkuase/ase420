"""
AbstractDisplay class for Template Method Pattern Example

This abstract class defines the template method and abstract methods
that subclasses must implement. It demonstrates how the Template Method
pattern defines the skeleton of an algorithm while letting subclasses
override specific steps.

This is the "Abstract Class" in the Template Method pattern.
"""

from abc import ABC, abstractmethod


class AbstractDisplay(ABC):
    """
    Abstract class that defines the template method pattern.
    
    The template method (display) defines the algorithm structure,
    while abstract methods (open, print, close) are implemented by subclasses.
    """
    
    @abstractmethod
    def open(self) -> None:
        """
        Abstract method to be implemented by subclasses.
        This method should handle the opening/initialization step.
        """
        pass
    
    @abstractmethod
    def print(self) -> None:
        """
        Abstract method to be implemented by subclasses.
        This method should handle the main printing step.
        """
        pass
    
    @abstractmethod
    def close(self) -> None:
        """
        Abstract method to be implemented by subclasses.
        This method should handle the closing/finalization step.
        """
        pass
    
    def display(self) -> None:
        """
        Template method that defines the algorithm skeleton.
        
        This method cannot be overridden (equivalent to Java's 'final').
        It defines the sequence of steps:
        1. open()
        2. print() (repeated 5 times)
        3. close()
        
        The actual implementation of each step is provided by subclasses.
        """
        self.open()
        for i in range(5):
            self.print()
        self.close()
    
    def __str__(self) -> str:
        """String representation of the AbstractDisplay."""
        return f"{self.__class__.__name__} (Template Method Pattern)"
