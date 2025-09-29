from state import State

class DayState(State):
    """Concrete state for daytime (9:00-17:00) behavior."""
    
    # Singleton instance
    _instance = None
    
    @classmethod
    def get_instance(cls):
        """Get singleton instance of DayState."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def do_use(self, context):
        """Handle safe usage during daytime - normal operation."""
        context.record_log("Safe used (normal daytime operation)")
    
    def do_alarm(self, context):
        """Handle emergency alarm during daytime."""
        context.call_security_center("Emergency alarm activated (daytime)")
    
    def do_phone(self, context):
        """Handle phone call during daytime - forward to security."""
        context.call_security_center("📞 Normal call forwarded to security (daytime)")
    
    def do_clock(self, context, hour):
        """Handle time changes - transition to night state if needed."""
        # Transition to night state if it's outside business hours
        if hour < 9 or hour >= 17:
            from night_state import NightState  # Import here to avoid circular imports
            print(f"Time is {hour:02d}:00 - Switching to NIGHT mode")
            context.change_state(NightState.get_instance())
    
    def __str__(self):
        return "DayState (9:00-17:00) - Normal Operations"
