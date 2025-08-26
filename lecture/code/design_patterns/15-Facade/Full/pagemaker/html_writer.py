"""
Facade Pattern - HtmlWriter Subsystem Component
This class handles HTML file generation for the page creation system.
"""

from typing import TextIO


class HtmlWriter:
    """
    HTML writer utility class that generates HTML content.
    This is part of the complex subsystem that the facade simplifies.
    """
    
    def __init__(self, writer: TextIO):
        """
        Initialize the HTML writer with a file writer.
        
        Args:
            writer (TextIO): File writer object to write HTML content to
        """
        self.writer = writer
    
    def title(self, title: str):
        """
        Write the HTML document title and header.
        
        Args:
            title (str): The title for the HTML page
        """
        self.writer.write("<!DOCTYPE html>\n")
        self.writer.write("<html>\n")
        self.writer.write("<head>\n")
        self.writer.write(f"<title>{title}</title>\n")
        self.writer.write("</head>\n")
        self.writer.write("<body>\n")
        self.writer.write(f"<h1>{title}</h1>\n")
    
    def paragraph(self, msg: str):
        """
        Write a paragraph element.
        
        Args:
            msg (str): The paragraph content
        """
        self.writer.write(f"<p>{msg}</p>\n")
    
    def link(self, href: str, caption: str):
        """
        Write a link element.
        
        Args:
            href (str): The URL for the link
            caption (str): The text to display for the link
        """
        self.paragraph(f'<a href="{href}">{caption}</a>')
    
    def mailto(self, mailaddr: str, username: str):
        """
        Write an email link.
        
        Args:
            mailaddr (str): The email address
            username (str): The username to display
        """
        self.link(f"mailto:{mailaddr}", username)
    
    def close(self):
        """
        Close the HTML document and the file writer.
        """
        self.writer.write("</body>\n")
        self.writer.write("</html>\n")
        self.writer.close()
