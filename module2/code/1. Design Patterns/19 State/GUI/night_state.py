from state import State

class NightState(State):
    """Concrete state representing nighttime operation (17:00-9:00).
    
    During nighttime (security mode):
    - Safe usage triggers an emergency alert (unauthorized access)
    - Emergency alarms call the security center
    - Phone calls are recorded for security review instead of being forwarded
    
    This class implements the Singleton pattern to ensure only one instance exists.
    """
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @staticmethod
    def get_instance():
        """Get the singleton instance of NightState."""
        if NightState._instance is None:
            NightState._instance = NightState()
        return NightState._instance
    
    def do_clock(self, context, hour):
        """Check if we need to transition to day state."""
        if 9 <= hour < 17:
            from day_state import DayState
            context.change_state(DayState.get_instance())
    
    def do_use(self, context):
        """Handle safe usage during nighttime - EMERGENCY! Unauthorized access."""
        context.call_security_center("EMERGENCY: Nighttime safe usage!")
    
    def do_alarm(self, context):
        """Handle emergency alarm during nighttime."""
        context.call_security_center("Emergency alarm (Nighttime)")
    
    def do_phone(self, context):
        """Handle phone calls during nighttime - record for security review."""
        context.record_log("Nighttime call recorded")
    
    def __str__(self):
        return "[Nighttime]"
