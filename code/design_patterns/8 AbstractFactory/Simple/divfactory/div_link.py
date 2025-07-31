from factory.link import Link


class DivLink(Link):
  
  def __init__(self, caption, url):
    super().__init__(caption, url)
  
  def make_html(self):
    return f'<div class="LINK"><a href="{self.url}">{self.caption}</a></div>\n'
