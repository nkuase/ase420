from factory.page import Page


class ListPage(Page):
  
  def __init__(self, title, author):
    super().__init__(title, author)
  
  def make_html(self):
    html_parts = [
      "<!DOCTYPE html>\n",
      f"<html><head><title>{self.title}</title></head>\n",
      "<body>\n",
      f"<h1>{self.title}</h1>\n",
      "<ul>\n"
    ]
    
    for item in self.content:
      html_parts.append(item.make_html())
    
    html_parts.extend([
      "</ul>\n",
      f"<hr><address>{self.author}</address>\n",
      "</body></html>\n"
    ])
    
    return "".join(html_parts)
