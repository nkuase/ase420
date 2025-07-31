from parse_exception import ParseException

class Context:
  def __init__(self, text):
    self.tokens = text.split()
    self.index = 0
    self.last_token = None
    self.next_token()
  
  def next_token(self):
    if self.index < len(self.tokens):
      self.last_token = self.tokens[self.index]
      self.index += 1
    else:
      self.last_token = None
    
    return self.last_token
  
  def current_token(self):
    return self.last_token
  
  def skip_token(self, expected_token):
    current = self.current_token()
    
    if current is None:
      raise ParseException(f"Error: '{expected_token}' is expected, but no more tokens found.")
    elif current != expected_token:
      raise ParseException(f"Error: '{expected_token}' is expected, but '{current}' is found.")
    
    self.next_token()
  
  def current_number(self):
    current = self.current_token()
    
    if current is None:
      raise ParseException("Error: No more tokens.")
    
    try:
      return int(current)
    except ValueError as e:
      raise ParseException(f"Error: Cannot convert '{current}' to number: {e}")
  
  def has_more_tokens(self):
    return self.current_token() is not None
  
  def get_remaining_tokens(self):
    if self.index <= len(self.tokens):
      return self.tokens[self.index-1:]
    return []
  
  def __str__(self):
    remaining = len(self.tokens) - self.index + 1
    return f"Context(current='{self.current_token()}', remaining={remaining})"
