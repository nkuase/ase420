class Label:
    """Label class for displaying text"""
    
    def __init__(self, label: str):
        self.label = label
        
    def display(self):
        """Display the label"""
        print(f"display: {self.label}")
        
    def __str__(self):
        return f'"{self.label}"'
