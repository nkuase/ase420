"""
Visitor Pattern - Concrete Visitor (ListVisitor)
This visitor displays the file system structure in a hierarchical list format.
"""

from visitor import Visitor
from file import File
from directory import Directory


class ListVisitor(Visitor):
    """
    Concrete visitor that displays the file system structure.
    Shows files and directories with their full paths.
    """
    
    def __init__(self):
        """Initialize the visitor with an empty current directory path."""
        self.current_dir = ""
    
    def visit_file(self, file: File):
        """
        Visit a file and display its path and details.
        
        Args:
            file (File): The file to visit
        """
        print(f"{self.current_dir}/{file}")
    
    def visit_directory(self, directory: Directory):
        """
        Visit a directory and recursively visit all its contents.
        
        Args:
            directory (Directory): The directory to visit
        """
        print(f"{self.current_dir}/{directory}")
        
        # Save current directory path
        saved_dir = self.current_dir
        
        # Update current path to include this directory
        self.current_dir = f"{self.current_dir}/{directory.get_name()}"
        
        # Visit all entries in this directory
        for entry in directory:
            entry.accept(self)
        
        # Restore previous directory path
        self.current_dir = saved_dir
