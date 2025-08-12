from builder import Builder


class TextBuilder(Builder):
  
  def __init__(self):
    self.buffer = []
  
  def make_title(self, title):
    self.buffer.append("=" * 30)
    self.buffer.append(f"[{title}]")
    self.buffer.append("")
  
  def make_string(self, string):
    self.buffer.append(f"■ {string}")
    self.buffer.append("")
  
  def make_items(self, items):
    for item in items:
      self.buffer.append(f"　- {item}")
    self.buffer.append("")
  
  def close(self):
    self.buffer.append("=" * 30)
  
  def get_text_result(self):
    return "\n".join(self.buffer)
