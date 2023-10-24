# interface
class Command(object):
  def execute(self): pass

class Receiver(object):
  def __str__(self):
    return "editor"
  def paste(self):
    print("Doing the paste action!")
  def copy(self):
    print("Doing the copy action!")
  
class Invoker(object): 
  def set_command(self, command):
    self.command = command

# Implementations 
class CopyCommand(Command):  
  def execute(self, receiver, params):
    print(f"To ({receiver}): copy {params}")    
    receiver.copy()

class PasteCommand(Command):    
  def execute(self, receiver, params):
    print(f"To ({receiver}): copy {params}")
    receiver.paste()

class Button(Invoker): pass
class Editor(Receiver): pass

# Driver  
## Invoker (button) initiating a request (command) to a receiver (editor)
button1 = Button()
button2 = Button()
receiver = Editor()

copy = CopyCommand()
button1.set_command(copy) # when button is clicked, copy command is created

paste = PasteCommand()
button2.set_command(paste)

## copy line 1
copy.execute(receiver, 'line 1') # copy command sends a command to the receiver
## paste
paste.execute(receiver, 'line 3')
