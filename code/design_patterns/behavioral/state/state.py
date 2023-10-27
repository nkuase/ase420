# interfaces
class State(object):
    def click_stop(self): pass
    def click_play(self): pass
    def click_record(self): pass

# Implementations


class RecordState(State):
    def __str__(self): return "Record state"
    def click_stop(self): return StopState()
    def click_play(self): pass
    def click_record(self): return RecordState()


class PlayState(State):
    def __str__(self): return "Play state"
    def click_stop(self): return StopState()
    def click_play(self): pass
    def click_record(self): return RecordState()


class StopState(State):
    def __str__(self): return "Stop state"
    def click_stop(self): pass
    def click_play(self): return PlayState()
    def click_record(self): pass

# Client


class Player(object):
    def __init__(self):
        self.state = StopState()

    def change_state(self, state):
        if state is not None:
            print(f"Changing state to {state}")
            self.state = state

    def click_stop(self):
        self.change_state(self.state.click_stop())

    def click_play(self):
        self.change_state(self.state.click_play())

    def click_record(self):
        self.change_state(self.state.click_record())


# Driver
p = Player()
p.click_play()
p.click_stop()
p.click_record()
p.click_play()  # This will be ignored as there is no state transition
p.click_stop()
