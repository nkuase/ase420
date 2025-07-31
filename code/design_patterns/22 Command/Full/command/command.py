"""
Command Pattern - Command Interface
This interface defines the contract for all command objects.
Commands encapsulate a request as an object.
"""

from abc import ABC, abstractmethod


class Command(ABC):
    """
    Abstract command interface that defines the execute method.
    All concrete commands must implement this interface.
    """
    
    @abstractmethod
    def execute(self):
        """
        Execute the command.
        This method encapsulates the action to be performed.
        """
        pass
