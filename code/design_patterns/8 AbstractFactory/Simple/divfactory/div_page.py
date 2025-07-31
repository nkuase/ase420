from factory.page import Page


class DivPage(Page):
  
  def __init__(self, title, author):
    super().__init__(title, author)
  
  def make_html(self):
    html_parts = [
      "<!DOCTYPE html>\n",
      f"<html><head><title>{self.title}</title><style>\n",
      "div.TRAY { padding:0.5em; margin-left:5em; border:1px solid black; }\n",
      "div.LINK { padding:0.5em; background-color: lightgray; }\n",
      "</style></head><body>\n",
      f"<h1>{self.title}</h1>\n"
    ]
    
    for item in self.content:
      html_parts.append(item.make_html())
    
    html_parts.extend([
      f"<hr><address>{self.author}</address>\n",
      "</body></html>\n"
    ])
    
    return "".join(html_parts)
