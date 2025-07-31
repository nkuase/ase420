"""
State Pattern - Concrete State (NightState)
This class represents the nighttime state of the security system.
It implements different behaviors for nighttime operations with heightened security.
"""

from state import State
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from context import Context


class NightState(State):
    """
    Concrete state representing nighttime operations (17:00 - 9:00).
    During nighttime, security is heightened and some operations trigger alerts.
    """
    
    _instance = None
    
    def __new__(cls):
        """Implement singleton pattern."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @staticmethod
    def get_instance() -> 'NightState':
        """
        Get the singleton instance of NightState.
        
        Returns:
            NightState: The singleton instance
        """
        if NightState._instance is None:
            NightState._instance = NightState()
        return NightState._instance
    
    def do_clock(self, context: 'Context', hour: int):
        """
        Handle time setting. Transition to day state during business hours.
        
        Args:
            context (Context): The context object
            hour (int): The current hour
        """
        if 9 <= hour < 17:
            # Import here to avoid circular dependency
            from day_state import DayState
            context.change_state(DayState.get_instance())
    
    def do_use(self, context: 'Context'):
        """
        Handle safe usage during nighttime - emergency alert!
        
        Args:
            context (Context): The context object
        """
        context.call_security_center("EMERGENCY: Nighttime safe usage!")
    
    def do_alarm(self, context: 'Context'):
        """
        Handle alarm during nighttime - security alert.
        
        Args:
            context (Context): The context object
        """
        context.call_security_center("Emergency alarm (Nighttime)")
    
    def do_phone(self, context: 'Context'):
        """
        Handle phone call during nighttime - record the call.
        
        Args:
            context (Context): The context object
        """
        context.record_log("Nighttime call recorded")
    
    def __str__(self) -> str:
        """String representation of the state."""
        return "[Nighttime]"
