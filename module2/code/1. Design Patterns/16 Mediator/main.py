"""
Mediator Pattern Demonstration

This shows how the complete Mediator pattern works with proper abstractions
that match the UML diagram structure.
"""

from concrete_mediator import SimpleDialog

def mediator():
    # Creating the mediator (which creates colleagues)
    dialog = SimpleDialog()
    
    # Initial state - TextBox
    text = dialog.textbox.get_text()
    print(text)
    
    dialog.button.click()

if __name__ == "__main__":
    mediator() 
