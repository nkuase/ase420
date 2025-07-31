# interface
class Memento(object):
  def restore(self): pass
class Originator(object):
  def save(self): pass
class Caretaker(object):
  def undo(self): pass

# Implementations
class SnapShot(Memento):  
  def __init__(self, state):
    self.state = state
  def restore(self, editor):
    editor.set_state(self.state)
    
class Editor(Originator):
  def set_state(self, state):
    self.state = state
  def save(self):
    return SnapShot(self.state)
  def print_state(self):
    print(f"Current editor state is {self.state}")

class Command(Caretaker):
  def __init__(self):
    self.snapshot = None
  def make_backup(self, snapshot):
    self.snapshot = snapshot
  def undo(self, editor):
    self.snapshot.restore(editor)
    
# Driver
editor = Editor() 
editor.set_state(1) # state 1
editor.print_state()

snapshot = editor.save() # take a snapshot to store state 1
caretaker = Command() 
caretaker.make_backup(snapshot)

editor.set_state(2) # state is now changed to 2
editor.print_state()

caretaker.undo(editor)
editor.print_state()
    