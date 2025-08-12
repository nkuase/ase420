from Label import Label
from NullLabel import NullLabel

class Person:
    """Person class using Null Object pattern (after refactoring)"""
    
    def __init__(self, name: Label, mail: Label = None):
        self.name = name
        self.mail = mail if mail is not None else NullLabel()
        
    def display(self):
        """Display person info - no null checks needed"""
        self.name.display()
        self.mail.display()
            
    def __str__(self):
        """String representation - no null checks needed"""
        return f"[ Person: name={self.name} mail={self.mail} ]"
