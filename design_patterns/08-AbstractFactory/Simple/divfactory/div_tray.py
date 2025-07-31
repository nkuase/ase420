from factory.tray import Tray


class DivTray(Tray):
  
  def __init__(self, caption):
    super().__init__(caption)
  
  def make_html(self):
    html_parts = [
      f"<p><b>{self.caption}</b></p>\n",
      '<div class="TRAY">'
    ]
    
    for item in self.tray:
      html_parts.append(item.make_html())
    
    html_parts.append("</div>\n")
    
    return "".join(html_parts)
