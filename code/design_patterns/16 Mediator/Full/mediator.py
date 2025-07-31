"""
Mediator Pattern - Mediator Interface
This interface defines the contract for mediators that coordinate colleague objects.
"""

from abc import ABC, abstractmethod


class Mediator(ABC):
    """
    Abstract mediator interface that defines how colleagues communicate.
    The mediator encapsulates how a set of objects interact with each other.
    """
    
    @abstractmethod
    def create_colleagues(self):
        """
        Create and initialize all colleague objects.
        """
        pass
    
    @abstractmethod
    def colleague_changed(self):
        """
        Called when a colleague's state changes.
        The mediator decides what actions to take based on the change.
        """
        pass
