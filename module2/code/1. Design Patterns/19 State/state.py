"""
Abstract State class for the State Design Pattern

This defines the interface that all concrete states must implement.
Each method represents a different action that can be performed,
but the behavior will vary depending on the current state.
"""

from abc import ABC, abstractmethod

class State(ABC):
    """Abstract base class for all states in the State pattern."""
    
    @abstractmethod
    def do_use(self, context):
        """Handle safe usage - behavior varies by state."""
        pass
    
    @abstractmethod
    def do_alarm(self, context):
        """Handle emergency alarm - behavior varies by state."""
        pass
    
    @abstractmethod
    def do_phone(self, context):
        """Handle phone call - behavior varies by state."""
        pass
    
    @abstractmethod
    def do_clock(self, context, hour):
        """Handle time change - may trigger state transitions."""
        pass
    
    def __str__(self):
        """Return a string representation of the state."""
        return self.__class__.__name__
