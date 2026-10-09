from day_state import DayState

class SecuritySystem:
    """Context class that delegates behavior to current state."""
    
    def __init__(self, name="Security System"):
        self.name = name
        self.state = DayState.get_instance()  # Start in day state
        self.current_time = "00:00"
        self.log_entries = []
        
        print(f"🔒 {self.name} initialized")
        print(f"📍 Initial state: {self.state}")
    
    # Public interface methods (called by clients)
    
    def use_safe(self):
        """User wants to use the safe."""
        print(f"\nUser action: USE SAFE at {self.current_time}")
        self.state.do_use(self)
    
    def trigger_alarm(self):
        """Emergency alarm is triggered."""
        print(f"\nUser action: EMERGENCY ALARM at {self.current_time}")
        self.state.do_alarm(self)
    
    def make_phone_call(self):
        """User makes a phone call."""
        print(f"\nUser action: PHONE CALL at {self.current_time}")
        self.state.do_phone(self)
    
    def set_time(self, hour):
        """Set the current time (may trigger state transitions)."""
        self.current_time = f"{hour:02d}:00"
        print(f"\nTime updated to: {self.current_time}")
        self.state.do_clock(self, hour)
    
    # Context interface methods (called by states)
    
    def change_state(self, new_state):
        """Change to a new state."""
        old_state = self.state
        self.state = new_state
        print(f"🔄 State transition: {old_state} → {new_state}")
    
    def record_log(self, message):
        """Record a log entry."""
        log_entry = f"[{self.current_time}] {message}"
        self.log_entries.append(log_entry)
        print(f"📝 LOG: {message}")
    
    def call_security_center(self, message):
        """Call the security center with a message."""
        log_entry = f"[{self.current_time}] SECURITY CALL: {message}"
        self.log_entries.append(log_entry)
        print(f"📞 SECURITY CALL: {message}")
    
    # Utility methods
    
    def get_current_state(self):
        """Get the current state."""
        return self.state
    
    def show_log(self):
        """Display all log entries."""
        print(f"\n📋 System Log for {self.name}:")
        print("=" * 60)
        for entry in self.log_entries:
            print(entry)
        print("=" * 60)
    
    def __str__(self):
        return f"{self.name} [Current state: {self.state}]"
