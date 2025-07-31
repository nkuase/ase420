from State import State
from StateStopped import StateStopped
from StateLogging import StateLogging

class Logger:
    def __init__(self): self._state = StateStopped()
    def get_state(self): return self._state
    def set_state(self, state): self._state = state
    def start(self): 
        self._state.start()
        self.set_state(StateLogging())
    def stop(self): 
        self._state.stop()
        self.set_state(StateStopped())
    def log(self, info: str): 
        self._state.log(info)
