"""
State Pattern - Context Interface
This interface defines the contract for context objects that use states.
The context delegates state-specific behavior to the current state object.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from state import State


class Context(ABC):
    """
    Abstract context interface that defines how the context interacts with states.
    The context maintains a reference to a state object and delegates
    state-specific behavior to it.
    """
    
    @abstractmethod
    def set_clock(self, hour: int):
        """
        Set the current time.
        
        Args:
            hour (int): The current hour (0-23)
        """
        pass
    
    @abstractmethod
    def change_state(self, state: 'State'):
        """
        Change to a new state.
        
        Args:
            state (State): The new state to transition to
        """
        pass
    
    @abstractmethod
    def call_security_center(self, msg: str):
        """
        Call the security center with a message.
        
        Args:
            msg (str): The message to send to security
        """
        pass
    
    @abstractmethod
    def record_log(self, msg: str):
        """
        Record a log message.
        
        Args:
            msg (str): The message to log
        """
        pass
