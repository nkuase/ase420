"""
Concrete Colleagues - Simple Button and TextBox

These are concrete implementations of the Colleague interface.
They are very simple but follow the proper pattern structure.
"""

from colleague import Colleague


class Button(Colleague):
    def __init__(self, name, mediator=None):
        super().__init__(mediator)
        self.name = name
        print(f"Button '{name}' created")
    
    def click(self):
        """User clicks the button"""
        print(f"Button '{self.name}' was clicked!")
        self.notify_mediator("clicked")  # Tell mediator what happened
    
    def enable(self):
        """Enable this button"""
        print(f"Button '{self.name}' enabled")
    
    def disable(self):
        """Disable this button"""
        print(f"Button '{self.name}' disabled")


class TextBox(Colleague):
    """
    Simple TextBox colleague.
    
    Can hold text and be cleared. Notifies mediator when text changes.
    This matches the UML diagram's ConcreteColleague2.
    """
    
    def __init__(self, mediator=None):
        super().__init__(mediator)
        self.text = "Hello World"
        print(f"TextBox created with text: '{self.text}'")
    
    def set_text(self, text):
        """Set the text content"""
        self.text = text
        print(f"TextBox text set to: '{self.text}'")
        self.notify_mediator("text_changed")  # Tell mediator what happened
    
    def clear(self):
        """Clear the text"""
        self.text = ""
        print(f"TextBox cleared")
        self.notify_mediator("text_changed")  # Tell mediator what happened
    
    def get_text(self):
        """Get current text"""
        return self.text

