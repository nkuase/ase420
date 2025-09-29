"""
Abstract Mediator - Base class for all mediators

This defines the interface that all concrete mediators must implement.
"""

from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass

