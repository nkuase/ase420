class Context:
    """Base class for context in the State pattern.
    
    The context maintains a reference to a state object and delegates
    state-specific behavior to the current state object.
    
    This class defines the interface that concrete contexts should implement.
    Instead of using ABC (which causes metaclass conflicts with PyQt6), 
    we use NotImplementedError to enforce the interface contract.
    """
    
    def set_clock(self, hour):
        """Update the current time display."""
        raise NotImplementedError("Subclasses must implement set_clock()")
    
    def change_state(self, state):
        """Change the current state of the system."""
        raise NotImplementedError("Subclasses must implement change_state()")
    
    def call_security_center(self, msg):
        """Send a message to the security center."""
        raise NotImplementedError("Subclasses must implement call_security_center()")
    
    def record_log(self, msg):
        """Record a message in the system log."""
        raise NotImplementedError("Subclasses must implement record_log()")
