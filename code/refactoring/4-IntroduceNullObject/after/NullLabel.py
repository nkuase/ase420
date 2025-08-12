from Label import Label

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
