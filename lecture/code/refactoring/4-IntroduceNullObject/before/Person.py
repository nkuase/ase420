from typing import Optional
from Label import Label

class Person:
    """Person class with null checks (before refactoring)"""
    
    def __init__(self, name: Label, mail: Optional[Label] = None):
        self.name = name
        self.mail = mail
        
    def display(self):
        """Display person info with null checks"""
        if self.name is not None:
            self.name.display()
        if self.mail is not None:
            self.mail.display()
            
    def __str__(self):
        """String representation with null checks"""
        result = "[ Person:"
        
        result += " name="
        if self.name is None:
            result += '"(none)"'
        else:
            result += str(self.name)
            
        result += " mail="
        if self.mail is None:
            result += '"(none)"'
        else:
            result += str(self.mail)
            
        result += " ]"
        
        return result
