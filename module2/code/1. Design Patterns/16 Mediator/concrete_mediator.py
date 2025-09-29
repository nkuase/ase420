"""
Concrete Mediator - Simple Dialog that coordinates Button and TextBox

This implements the abstract Mediator interface and defines
how Button and TextBox should interact with each other.
"""

from mediator import Mediator
from concrete_colleagues import Button, TextBox


class SimpleDialog(Mediator):
    def __init__(self):
        # Create colleagues and set their mediator
        self.button = Button("Clear", self)
        self.textbox = TextBox(self)
        
        # Initial coordination
        self._update_button_state()
        print("Simple Dialog ready\n-----------")
    
    def notify(self, sender, event):
        print(f"Mediator received: {event} from {type(sender).__name__}")
        
        if sender == self.button and event == "clicked":
            # Button was clicked → clear textbox
            self.textbox.clear()
        
        elif sender == self.textbox and event == "text_changed":
            # Text changed → update button state
            self._update_button_state()
    
    def _update_button_state(self):
        """Update button based on textbox content"""
        if self.textbox.get_text():
            self.button.enable()   # Has text → enable button
        else:
            self.button.disable()  # No text → disable button
