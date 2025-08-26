"""
Observer interface for Observer Pattern Example

This interface defines the contract that all observers must follow.
Observers are notified when the subject (observable) they're watching changes.

This is the "Observer" interface in the Observer pattern.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

# Use TYPE_CHECKING to avoid circular imports
if TYPE_CHECKING:
    from number_generator import NumberGenerator


class Observer(ABC):
    """
    Abstract observer interface for the Observer pattern.
    
    This interface defines the update method that all concrete observers
    must implement. When the subject changes, it notifies all registered
    observers by calling their update method.
    """
    
    @abstractmethod
    def update(self, generator: 'NumberGenerator') -> None:
        """
        Update method called when the observed subject changes.
        
        This method is called by the subject (NumberGenerator) to notify
        the observer about changes. Each concrete observer implements
        this method to define how it responds to changes.
        
        Args:
            generator (NumberGenerator): The subject that changed
        """
        pass
