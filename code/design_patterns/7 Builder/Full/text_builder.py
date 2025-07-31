"""
Builder Pattern - Text Builder
Concrete builder that creates documents in plain text format.
"""

from typing import List
from builder import Builder


class TextBuilder(Builder):
    """
    Concrete builder that creates documents in plain text format.
    Uses simple text formatting with borders and bullet points.
    """
    
    def __init__(self):
        """Initialize the text builder with an empty string buffer."""
        self.buffer = []
    
    def make_title(self, title: str):
        """
        Create a title with decorative borders.
        
        Args:
            title (str): The title text
        """
        self.buffer.append("=" * 30)
        self.buffer.append(f"[{title}]")
        self.buffer.append("")
    
    def make_string(self, string: str):
        """
        Add a string section with a bullet point marker.
        
        Args:
            string (str): The string content
        """
        self.buffer.append(f"■ {string}")
        self.buffer.append("")
    
    def make_items(self, items: List[str]):
        """
        Add a list of items with indentation and dashes.
        
        Args:
            items (List[str]): List of item strings
        """
        for item in items:
            self.buffer.append(f"　- {item}")
        self.buffer.append("")
    
    def close(self):
        """Add a closing border to the document."""
        self.buffer.append("=" * 30)
    
    def get_text_result(self) -> str:
        """
        Get the final text result.
        
        Returns:
            str: The complete text document
        """
        return "\n".join(self.buffer)
