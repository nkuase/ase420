"""
Div Factory - Creates HTML using <div> tags
==========================================
This factory creates components that render as HTML divs.
"""

from base_classes import Link, Tray, Page, Factory


class DivLink(Link):
    """Link that renders as <div><a href="">text</a></div>"""
    def make_html(self):
        return f'<div class="LINK"><a href="{self.url}">{self.caption}</a></div>\n'


class DivTray(Tray):
    """Tray that renders as grouped divs"""
    def make_html(self):
        html = f'<p><b>{self.caption}</b></p>\n<div class="TRAY">\n'
        for item in self.items:
            html += item.make_html()
        html += '</div>\n'
        return html


class DivPage(Page):
    """Page that renders everything as HTML divs"""
    def make_html(self):
        html = f'<html><head><title>{self.title}</title></head>\n'
        html += f'<body>\n<h1>{self.title}</h1>\n'
        
        for item in self.content:
            html += item.make_html()
        
        html += f'<hr><address>{self.author}</address>\n</body></html>\n'
        return html


class DivFactory(Factory):
    """Factory that creates Div-style HTML components"""
    def create_link(self, caption, url):
        return DivLink(caption, url)
    
    def create_tray(self, caption):
        return DivTray(caption)
    
    def create_page(self, title, author):
        return DivPage(title, author)
