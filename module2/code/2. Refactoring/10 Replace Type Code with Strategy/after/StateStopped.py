from State import State

class StateStopped(State):
    """Stopped state implementation"""
    
    def get_type_code(self) -> int:
        # Import here to avoid circular import
        from Logger import Logger
        return Logger.STATE_STOPPED
