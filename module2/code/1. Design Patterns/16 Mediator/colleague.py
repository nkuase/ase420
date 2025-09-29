"""
Abstract Colleague - Base class for all colleagues

This defines the interface that all concrete colleagues must implement.
"""

from abc import ABC, abstractmethod


class Colleague(ABC):
    """
    Abstract Colleague interface.
    
    All colleagues that work with a mediator must extend this class.
    This matches the UML diagram's Colleague class.
    """
    
    def __init__(self, mediator=None):
        """Initialize with optional mediator reference"""
        self._mediator = mediator
    
    def set_mediator(self, mediator):
        """Set the mediator for this colleague"""
        self._mediator = mediator
    
    def notify_mediator(self, event):
        """Notify the mediator that something happened"""
        if self._mediator:
            self._mediator.notify(self, event)

