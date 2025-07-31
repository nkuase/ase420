"""
State Pattern - Concrete State (DayState)
This class represents the daytime state of the security system.
It implements different behaviors for daytime operations.
"""

from state import State
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from context import Context


class DayState(State):
    """
    Concrete state representing daytime operations (9:00 - 17:00).
    During daytime, normal operations are allowed and security is relaxed.
    """
    
    _instance = None
    
    def __new__(cls):
        """Implement singleton pattern."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @staticmethod
    def get_instance() -> 'DayState':
        """
        Get the singleton instance of DayState.
        
        Returns:
            DayState: The singleton instance
        """
        if DayState._instance is None:
            DayState._instance = DayState()
        return DayState._instance
    
    def do_clock(self, context: 'Context', hour: int):
        """
        Handle time setting. Transition to night state if outside business hours.
        
        Args:
            context (Context): The context object
            hour (int): The current hour
        """
        if hour < 9 or hour >= 17:
            # Import here to avoid circular dependency
            from night_state import NightState
            context.change_state(NightState.get_instance())
    
    def do_use(self, context: 'Context'):
        """
        Handle safe usage during daytime - normal operation.
        
        Args:
            context (Context): The context object
        """
        context.record_log("Safe used (Daytime)")
    
    def do_alarm(self, context: 'Context'):
        """
        Handle alarm during daytime - call security.
        
        Args:
            context (Context): The context object
        """
        context.call_security_center("Emergency alarm (Daytime)")
    
    def do_phone(self, context: 'Context'):
        """
        Handle phone call during daytime - normal call.
        
        Args:
            context (Context): The context object
        """
        context.call_security_center("Normal call (Daytime)")
    
    def __str__(self) -> str:
        """String representation of the state."""
        return "[Daytime]"
