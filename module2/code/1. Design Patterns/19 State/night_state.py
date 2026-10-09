from state import State

class NightState(State):
    # Singleton instance
    _instance = None
    
    @classmethod
    def get_instance(cls):
        """Get singleton instance of NightState."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def do_use(self, context):
        """Handle safe usage during nighttime - SECURITY ALERT!"""
        context.call_security_center("SECURITY ALERT: Unauthorized safe access detected at night!")
    
    def do_alarm(self, context):
        """Handle emergency alarm during nighttime."""
        context.call_security_center("Emergency alarm activated (nighttime)")
    
    def do_phone(self, context):
        """Handle phone call during nighttime - record instead of forward."""
        context.record_log("Phone call recorded for security review (nighttime)")
    
    def do_clock(self, context, hour):
        """Handle time changes - transition to day state if needed."""
        # Transition to day state if it's business hours
        if 9 <= hour < 17:
            from day_state import DayState  # Import here to avoid circular imports
            print(f"⏰ Time is {hour:02d}:00 - Switching to DAY mode")
            context.change_state(DayState.get_instance())
    
    def __str__(self):
        return "NightState (17:00-9:00) - High Security Mode"
