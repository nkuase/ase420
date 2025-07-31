from factory.tray import Tray


class ListTray(Tray):
  
  def __init__(self, caption):
    super().__init__(caption)
  
  def make_html(self):
    html_parts = ["<li>\n", self.caption, "\n<ul>\n"]
    
    for item in self.tray:
      html_parts.append(item.make_html())
    
    html_parts.extend(["</ul>\n", "</li>\n"])
    
    return "".join(html_parts)
