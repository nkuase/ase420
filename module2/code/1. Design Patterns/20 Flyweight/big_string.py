from big_char import BigChar
from big_char_factory import BigCharFactory

class BigString:
  def __init__(self, string):
    self.string = string
    factory = BigCharFactory.get_instance()
    
    self.bigchars = []
    for char in string:
      big_char = factory.get_big_char(char)
      self.bigchars.append(big_char)
  
  def print(self):
    lines = self._get_lines()
    for line in lines:
      print(line)
  
  def _get_lines(self):
    if not self.bigchars:
      return []
    
    char_lines = []
    for big_char in self.bigchars:
      fontdata = big_char.get_fontdata()
      lines = fontdata.split('\n')
      char_lines.append(lines)
    
    max_lines = max(len(lines) for lines in char_lines) if char_lines else 0
    
    result_lines = []
    for line_num in range(max_lines):
      combined_line = ""
      for char_line_list in char_lines:
        if line_num < len(char_line_list):
          combined_line += char_line_list[line_num]
        else:
          combined_line += " " * 16
      result_lines.append(combined_line.rstrip())
    
    return result_lines
  
  def get_string(self):
    return self.string
  
  def get_char_count(self):
    return len(self.bigchars)
  
  def __str__(self):
    return f"BigString('{self.string}')"
