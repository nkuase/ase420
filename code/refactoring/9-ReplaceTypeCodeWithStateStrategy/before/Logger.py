class Logger:
    """Logger class with type codes (before refactoring)"""
    
    STATE_STOPPED = 0
    STATE_LOGGING = 1
    
    def __init__(self):
        self.state = Logger.STATE_STOPPED
        
    def start(self):
        if self.state == Logger.STATE_STOPPED:
            print("** START LOGGING **")
            self.state = Logger.STATE_LOGGING
        elif self.state == Logger.STATE_LOGGING:
            # Do nothing
            pass
        else:
            print(f"Invalid state: {self.state}")
            
    def stop(self):
        if self.state == Logger.STATE_STOPPED:
            # Do nothing
            pass
        elif self.state == Logger.STATE_LOGGING:
            print("** STOP LOGGING **")
            self.state = Logger.STATE_STOPPED
        else:
            print(f"Invalid state: {self.state}")
            
    def log(self, info: str):
        if self.state == Logger.STATE_STOPPED:
            print(f"Ignoring: {info}")
        elif self.state == Logger.STATE_LOGGING:
            print(f"Logging: {info}")
        else:
            print(f"Invalid state: {self.state}")
