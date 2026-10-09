"""
Abstract Factory Pattern - Core Classes
======================================
This file contains the basic classes that all factories will use.
Keep it simple - just the essential structure.
"""

class Link:
    """A clickable link"""
    def __init__(self, caption, url):
        self.caption = caption
        self.url = url
    
    def make_html(self):
        # Will be implemented by subclasses (ListLink, DivLink)
        pass


class Tray:
    """Container that holds multiple items"""
    def __init__(self, caption):
        self.caption = caption
        self.items = []
    
    def add(self, item):
        """Add a link or another tray"""
        self.items.append(item)
    
    def make_html(self):
        # Will be implemented by subclasses (ListTray, DivTray)
        pass


class Page:
    """A complete HTML page"""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.content = []
    
    def add(self, item):
        """Add a tray to the page"""
        self.content.append(item)
    
    def make_html(self):
        # Will be implemented by subclasses (ListPage, DivPage)
        pass
    
    def printit(self):
        print(self.make_html())


class Factory:
    """Abstract Factory - creates families of related objects"""
    def create_link(self, caption, url): pass
    def create_tray(self, caption): pass
    def create_page(self, title, author): pass
