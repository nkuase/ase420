class Label:
    """Label class for displaying text (with null object support)"""
    
    def __init__(self, label: str):
        self.label = label
        
    def display(self):
        """Display the label"""
        print(f"display: {self.label}")
        
    def is_null(self) -> bool:
        """Check if this is a null object"""
        return False
        
    def __str__(self):
        return f'"{self.label}"'

class NullLabel(Label):
    """Null Object implementation for Label"""
    
    def __init__(self):
        super().__init__("(none)")
        
    def display(self):
        """Do nothing for null objects"""
        pass
        
    def is_null(self) -> bool:
        """This is a null object"""
        return True