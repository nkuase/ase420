from builder import Builder

class Director:
  
  def __init__(self, builder):
    self.builder = builder
  
  def construct(self):
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
