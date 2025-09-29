from State import State
from StateStopped import StateStopped
from StateLogging import StateLogging

class Logger:
    """Logger class using State pattern (after refactoring)"""
    
    STATE_STOPPED = 0
    STATE_LOGGING = 1
    
    def __init__(self):
        self.set_state(Logger.STATE_STOPPED)
        
    def get_state(self) -> int:
        return self._state.get_type_code()
        
    def set_state(self, state: int):
        if state == Logger.STATE_STOPPED:
            self._state = StateStopped()
        elif state == Logger.STATE_LOGGING:
            self._state = StateLogging()
        else:
            print(f"Invalid state: {state}")
            
    def start(self):
        if self.get_state() == Logger.STATE_STOPPED:
            print("** START LOGGING **")
            self.set_state(Logger.STATE_LOGGING)
        elif self.get_state() == Logger.STATE_LOGGING:
            # Do nothing
            pass
        else:
            print(f"Invalid state: {self.get_state()}")
            
    def stop(self):
        if self.get_state() == Logger.STATE_STOPPED:
            # Do nothing
            pass
        elif self.get_state() == Logger.STATE_LOGGING:
            print("** STOP LOGGING **")
            self.set_state(Logger.STATE_STOPPED)
        else:
            print(f"Invalid state: {self.get_state()}")
            
    def log(self, info: str):
        if self.get_state() == Logger.STATE_STOPPED:
            print(f"Ignoring: {info}")
        elif self.get_state() == Logger.STATE_LOGGING:
            print(f"Logging: {info}")
        else:
            print(f"Invalid state: {self.get_state()}")
