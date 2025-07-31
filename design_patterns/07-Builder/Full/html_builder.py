"""
Builder Pattern - HTML Builder
Concrete builder that creates documents in HTML format.
"""

from typing import List
from builder import Builder


class HTMLBuilder(Builder):
    """
    Concrete builder that creates documents in HTML format.
    Generates valid HTML with proper tags and structure.
    """
    
    def __init__(self):
        """Initialize the HTML builder with default filename and empty buffer."""
        self.filename = "untitled.html"
        self.buffer = []
    
    def make_title(self, title: str):
        """
        Create an HTML title with DOCTYPE, head, and h1 tags.
        
        Args:
            title (str): The title text
        """
        self.filename = f"{title}.html"
        self.buffer.extend([
            "<!DOCTYPE html>",
            "<html>",
            f"<head><title>{title}</title></head>",
            "<body>",
            f"<h1>{title}</h1>",
            ""
        ])
    
    def make_string(self, string: str):
        """
        Add a string as an HTML paragraph.
        
        Args:
            string (str): The string content
        """
        self.buffer.append(f"<p>{string}</p>")
        self.buffer.append("")
    
    def make_items(self, items: List[str]):
        """
        Add a list of items as an HTML unordered list.
        
        Args:
            items (List[str]): List of item strings
        """
        self.buffer.append("<ul>")
        for item in items:
            self.buffer.append(f"<li>{item}</li>")
        self.buffer.append("</ul>")
        self.buffer.append("")
    
    def close(self):
        """
        Close the HTML document and write to file.
        """
        self.buffer.extend([
            "</body>",
            "</html>"
        ])
        
        # Write the HTML content to file
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                f.write("\n".join(self.buffer))
        except IOError as e:
            print(f"Error writing file: {e}")
    
    def get_html_result(self) -> str:
        """
        Get the filename of the created HTML file.
        
        Returns:
            str: The filename of the HTML document
        """
        return self.filename
