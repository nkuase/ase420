from state import RedState

class TrafficLight:  # Context
    def __init__(self):
        self._state = RedState()
    
    def set_state(self, state):
        self._state = state
    
    def change(self):
        self._state.handle(self)