from state import State

class DayState(State):
    """Concrete state representing daytime operation (9:00-17:00).
    
    During daytime:
    - Safe usage is normal and gets logged
    - Emergency alarms call the security center
    - Phone calls are treated as normal calls to security
    
    This class implements the Singleton pattern to ensure only one instance exists.
    """
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @staticmethod
    def get_instance():
        """Get the singleton instance of DayState."""
        if DayState._instance is None:
            DayState._instance = DayState()
        return DayState._instance
    
    def do_clock(self, context, hour):
        """Check if we need to transition to night state."""
        if hour < 9 or hour >= 17:
            from night_state import NightState
            context.change_state(NightState.get_instance())
    
    def do_use(self, context):
        """Handle safe usage during daytime - normal operation."""
        context.record_log("Safe used (Daytime)")
    
    def do_alarm(self, context):
        """Handle emergency alarm during daytime."""
        context.call_security_center("Emergency alarm (Daytime)")
    
    def do_phone(self, context):
        """Handle phone calls during daytime - normal calls."""
        context.call_security_center("Normal call (Daytime)")
    
    def __str__(self):
        return "[Daytime]"
