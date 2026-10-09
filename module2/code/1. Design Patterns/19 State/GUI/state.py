from abc import ABC, abstractmethod

class State(ABC):
    """Abstract base class for all states in the State pattern.
    
    Each concrete state will implement these methods differently,
    demonstrating how the same action can have different behaviors
    depending on the current state.
    """
    
    @abstractmethod
    def do_clock(self, context, hour):
        """Handle time changes and potentially trigger state transitions."""
        pass
    
    @abstractmethod
    def do_use(self, context):
        """Handle safe usage action - behavior varies by state."""
        pass
    
    @abstractmethod
    def do_alarm(self, context):
        """Handle emergency alarm action - behavior varies by state."""
        pass
    
    @abstractmethod
    def do_phone(self, context):
        """Handle phone call action - behavior varies by state."""
        pass
