"""
Builder Pattern - Director
The Director class uses a Builder to construct a document.
It knows the sequence of construction but doesn't know the specific format.
"""

from builder import Builder


class Director:
    """
    Director class that orchestrates the document construction process.
    It uses a Builder object to create documents in a specific sequence.
    """
    
    def __init__(self, builder: Builder):
        """
        Initialize the director with a builder.
        
        Args:
            builder (Builder): The builder object to use for construction
        """
        self.builder = builder
    
    def construct(self):
        """
        Construct a document using the builder.
        This method defines the construction sequence and content.
        """
        self.builder.make_title("Greeting")
        
        self.builder.make_string("General greetings")
        self.builder.make_items([
            "How are you?",
            "Hello.",
            "Hi.",
        ])
        
        self.builder.make_string("Time-based greetings")
        self.builder.make_items([
            "Good morning.",
            "Good afternoon.",
            "Good evening.",
        ])
        
        self.builder.close()
