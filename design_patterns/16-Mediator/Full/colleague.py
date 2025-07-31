"""
Mediator Pattern - Colleague Interface
This interface defines the contract for colleague objects that interact through a mediator.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mediator import Mediator


class Colleague(ABC):
    """
    Abstract colleague interface for objects that interact through a mediator.
    Colleagues communicate with each other indirectly through the mediator.
    """
    
    @abstractmethod
    def set_mediator(self, mediator: 'Mediator'):
        """
        Set the mediator for this colleague.
        
        Args:
            mediator (Mediator): The mediator that will coordinate interactions
        """
        pass
    
    @abstractmethod
    def set_colleague_enabled(self, enabled: bool):
        """
        Enable or disable this colleague based on mediator's decision.
        
        Args:
            enabled (bool): True to enable, False to disable
        """
        pass
