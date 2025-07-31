from builder import Builder


class HTMLBuilder(Builder):
  
  def __init__(self):
    self.filename = "untitled.html"
    self.buffer = []
  
  def make_title(self, title):
    self.filename = f"{title}.html"
    self.buffer.extend([
      "<!DOCTYPE html>",
      "<html>",
      f"<head><title>{title}</title></head>",
      "<body>",
      f"<h1>{title}</h1>",
      ""
    ])
  
  def make_string(self, string):
    self.buffer.append(f"<p>{string}</p>")
    self.buffer.append("")
  
  def make_items(self, items):
    self.buffer.append("<ul>")
    for item in items:
      self.buffer.append(f"<li>{item}</li>")
    self.buffer.append("</ul>")
    self.buffer.append("")
  
  def close(self):
    self.buffer.extend([
      "</body>",
      "</html>"
    ])
    
    try:
      with open(self.filename, 'w', encoding='utf-8') as f:
        f.write("\n".join(self.buffer))
    except IOError as e:
      print(f"Error writing file: {e}")
  
  def get_html_result(self):
    return self.filename
