"""
List Factory - Creates HTML using <ul> and <li> tags
===================================================
This factory creates components that render as HTML lists.
"""

from base_classes import Link, Tray, Page, Factory


class ListLink(Link):
    """Link that renders as <li><a href="">text</a></li>"""
    def make_html(self):
        return f'  <li><a href="{self.url}">{self.caption}</a></li>\n'


class ListTray(Tray):
    """Tray that renders as nested <ul> lists"""
    def make_html(self):
        html = f'<li>\n{self.caption}\n<ul>\n'
        for item in self.items:
            html += item.make_html()
        html += '</ul>\n</li>\n'
        return html


class ListPage(Page):
    """Page that renders everything as HTML lists"""
    def make_html(self):
        html = f'<html><head><title>{self.title}</title></head>\n'
        html += f'<body>\n<h1>{self.title}</h1>\n<ul>\n'
        
        for item in self.content:
            html += item.make_html()
        
        html += f'</ul>\n<hr><address>{self.author}</address>\n</body></html>\n'
        return html


class ListFactory(Factory):
    """Factory that creates List-style HTML components"""
    def create_link(self, caption, url):
        return ListLink(caption, url)
    
    def create_tray(self, caption):
        return ListTray(caption)
    
    def create_page(self, title, author):
        return ListPage(title, author)
