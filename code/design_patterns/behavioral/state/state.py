# interfaces
class State(object):
  def __init__(self, player):
    self.player = player
  def click_stop(self): pass
  def click_play(self): pass
  def click_record(self): pass
  
# Implementations  
class RecordState(State):
  def __str__(self): return "Record state"
  def click_stop(self): self.player.change_state(StopState(self.player))
  def click_play(self): pass
  def click_record(self): pass
  
class PlayState(State):
  def __str__(self): return "Play state"  
  def click_stop(self): self.player.change_state(StopState(self.player))
  def click_play(self): pass
  def click_record(self): self.player.change_state(RecordState(self.player))  

class StopState(State):
  def __str__(self): return "Stop state"  
  def click_stop(self): pass
  def click_play(self): self.player.change_state(PlayState(self.player)) 
  def click_record(self): self.player.change_state(RecordState(self.player)) 

# Client
class Player(object):
  def __init__(self):
    self.state = StopState(self)
  def change_state(self, state):
    print(f"Changing state to {state}")
    self.state = state
  def click_stop(self): self.state.click_stop()
  def click_play(self): self.state.click_play()
  def click_record(self): self.state.click_record()     
    
# Driver    
p = Player()
p.click_play()
p.click_stop()
p.click_record()
p.click_play() # This will be ignored as there is no state transition
p.click_stop()