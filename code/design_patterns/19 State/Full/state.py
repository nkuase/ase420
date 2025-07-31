"""
State Pattern - State Interface
This interface defines the contract for concrete state classes.
Each state handles requests differently based on the current state.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from context import Context


class State(ABC):
    """
    Abstract state interface that defines the methods each concrete state must implement.
    Each method represents an action that can be performed, and the behavior
    depends on the current state.
    """
    
    @abstractmethod
    def do_clock(self, context: 'Context', hour: int):
        """
        Handle time setting. May trigger state transitions.
        
        Args:
            context (Context): The context object
            hour (int): The current hour (0-23)
        """
        pass
    
    @abstractmethod
    def do_use(self, context: 'Context'):
        """
        Handle safe usage request.
        
        Args:
            context (Context): The context object
        """
        pass
    
    @abstractmethod
    def do_alarm(self, context: 'Context'):
        """
        Handle alarm activation.
        
        Args:
            context (Context): The context object
        """
        pass
    
    @abstractmethod
    def do_phone(self, context: 'Context'):
        """
        Handle phone call request.
        
        Args:
            context (Context): The context object
        """
        pass
