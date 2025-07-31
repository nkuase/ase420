"""
NumberGenerator abstract class for Observer Pattern Example

This abstract class represents the subject (observable) in the Observer pattern.
It maintains a list of observers and notifies them when its state changes.

This is the "Subject/Observable" in the Observer pattern.
"""

from abc import ABC, abstractmethod
from typing import List
from observer import Observer


class NumberGenerator(ABC):
    """
    Abstract number generator that can be observed.
    
    This class implements the subject side of the Observer pattern.
    It maintains a list of observers and provides methods to add,
    remove, and notify observers when changes occur.
    """
    
    def __init__(self):
        """Initialize the number generator with an empty observer list."""
        self._observers: List[Observer] = []
    
    def add_observer(self, observer: Observer) -> None:
        """
        Add an observer to the list of observers.
        
        Args:
            observer (Observer): The observer to add
            
        Raises:
            TypeError: If observer doesn't implement Observer interface
        """
        if not isinstance(observer, Observer):
            raise TypeError("Observer must implement Observer interface")
        
        if observer not in self._observers:
            self._observers.append(observer)
    
    def delete_observer(self, observer: Observer) -> bool:
        """
        Remove an observer from the list of observers.
        
        Args:
            observer (Observer): The observer to remove
            
        Returns:
            bool: True if observer was found and removed, False otherwise
        """
        try:
            self._observers.remove(observer)
            return True
        except ValueError:
            return False
    
    def notify_observers(self) -> None:
        """
        Notify all registered observers about a change.
        
        This method is called whenever the state of the number generator
        changes. It iterates through all registered observers and calls
        their update method.
        """
        for observer in self._observers:
            observer.update(self)
    
    def get_observer_count(self) -> int:
        """
        Get the number of registered observers.
        
        Returns:
            int: The number of observers
        """
        return len(self._observers)
    
    def clear_observers(self) -> None:
        """Remove all observers."""
        self._observers.clear()
    
    @abstractmethod
    def get_number(self) -> int:
        """
        Get the current number.
        
        This method must be implemented by concrete subclasses
        to return the current number value.
        
        Returns:
            int: The current number
        """
        pass
    
    @abstractmethod
    def execute(self) -> None:
        """
        Execute the number generation process.
        
        This method must be implemented by concrete subclasses
        to define how numbers are generated and when observers
        should be notified.
        """
        pass
    
    def __str__(self) -> str:
        """String representation of the number generator."""
        return f"{self.__class__.__name__}(current={self.get_number()}, observers={len(self._observers)})"
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"{self.__class__.__name__}(observers={len(self._observers)})"
