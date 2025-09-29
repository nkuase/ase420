class ValueChangeEvent:
    """Event fired when a value changes"""
    
    def __init__(self, source):
        self.source = source
        
    def get_source(self):
        return self.source
