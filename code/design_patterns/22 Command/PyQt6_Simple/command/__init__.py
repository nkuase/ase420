"""
Command package for the Command design pattern implementation.

This package contains the abstract Command interface and concrete implementations
that demonstrate how to encapsulate requests as objects.
"""

from .command import Command
from .macro_command import MacroCommand

__all__ = ['Command', 'MacroCommand']
