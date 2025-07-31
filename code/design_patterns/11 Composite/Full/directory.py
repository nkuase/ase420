"""
Directory class for Composite Pattern Example

This class represents a composite node in the Composite pattern.
A directory can contain other entries (files or other directories).

This is a "Composite" in the Composite pattern.
"""

from typing import List, Iterator, Optional
from entry import Entry


class Directory(Entry):
    """
    Concrete implementation of Entry representing a directory.
    
    Directories are composite nodes in the file system hierarchy - they can
    contain other entries (files or subdirectories). They represent the
    "composite" objects in the Composite pattern that manage child components.
    """
    
    def __init__(self, name: str):
        """
        Initialize a directory with a name.
        
        Args:
            name (str): The name of the directory
        """
        self._name = name
        self._entries: List[Entry] = []
    
    def get_name(self) -> str:
        """
        Get the name of this directory.
        
        Returns:
            str: The directory name
        """
        return self._name
    
    def get_size(self) -> int:
        """
        Get the total size of this directory.
        
        The size is calculated as the sum of all contained entries' sizes.
        This demonstrates the Composite pattern's recursive behavior.
        
        Returns:
            int: The total size of all contained entries in bytes
        """
        total_size = 0
        for entry in self._entries:
            total_size += entry.get_size()
        return total_size
    
    def _print_list(self, prefix: str) -> None:
        """
        Print this directory and all its contents in a tree format.
        
        This method demonstrates the recursive nature of the Composite pattern.
        It prints the directory itself, then recursively prints all contained entries.
        
        Args:
            prefix (str): The prefix string for proper indentation
        """
        # Print this directory
        print(f"{prefix}/{self}")
        
        # Recursively print all contained entries
        for entry in self._entries:
            entry._print_list(f"{prefix}/{self._name}")
    
    def add(self, entry: Entry) -> 'Directory':
        """
        Add an entry to this directory.
        
        This method allows building the composite structure by adding
        child components. Returns self to allow method chaining.
        
        Args:
            entry (Entry): The entry (file or directory) to add
            
        Returns:
            Directory: This directory (for method chaining)
            
        Raises:
            TypeError: If entry is not an Entry instance
        """
        if not isinstance(entry, Entry):
            raise TypeError("Can only add Entry instances to directory")
        
        self._entries.append(entry)
        return self
    
    def remove(self, entry: Entry) -> bool:
        """
        Remove an entry from this directory.
        
        Args:
            entry (Entry): The entry to remove
            
        Returns:
            bool: True if the entry was found and removed, False otherwise
        """
        try:
            self._entries.remove(entry)
            return True
        except ValueError:
            return False
    
    def remove_by_name(self, name: str) -> bool:
        """
        Remove an entry by name.
        
        Args:
            name (str): The name of the entry to remove
            
        Returns:
            bool: True if an entry with the name was found and removed
        """
        for entry in self._entries:
            if entry.get_name() == name:
                self._entries.remove(entry)
                return True
        return False
    
    def find(self, name: str) -> Optional[Entry]:
        """
        Find an entry by name in this directory.
        
        Args:
            name (str): The name of the entry to find
            
        Returns:
            Optional[Entry]: The entry if found, None otherwise
        """
        for entry in self._entries:
            if entry.get_name() == name:
                return entry
        return None
    
    def get_entries(self) -> List[Entry]:
        """
        Get a copy of all entries in this directory.
        
        Returns:
            List[Entry]: List of all contained entries
        """
        return self._entries.copy()
    
    def get_files(self) -> List['File']:
        """
        Get all files (leaf nodes) in this directory.
        
        Returns:
            List[File]: List of all files in this directory
        """
        from file import File  # Import here to avoid circular imports
        return [entry for entry in self._entries if isinstance(entry, File)]
    
    def get_directories(self) -> List['Directory']:
        """
        Get all subdirectories in this directory.
        
        Returns:
            List[Directory]: List of all subdirectories
        """
        return [entry for entry in self._entries if isinstance(entry, Directory)]
    
    def get_total_files(self) -> int:
        """
        Get the total number of files in this directory and all subdirectories.
        
        This demonstrates recursive traversal of the composite structure.
        
        Returns:
            int: Total number of files in the entire subtree
        """
        from file import File  # Import here to avoid circular imports
        
        count = 0
        for entry in self._entries:
            if isinstance(entry, File):
                count += 1
            elif isinstance(entry, Directory):
                count += entry.get_total_files()
        return count
    
    def is_empty(self) -> bool:
        """
        Check if this directory is empty.
        
        Returns:
            bool: True if the directory contains no entries
        """
        return len(self._entries) == 0
    
    def __len__(self) -> int:
        """
        Get the number of direct entries in this directory.
        
        Returns:
            int: Number of direct child entries
        """
        return len(self._entries)
    
    def __iter__(self) -> Iterator[Entry]:
        """
        Make directory iterable over its entries.
        
        Returns:
            Iterator[Entry]: Iterator over contained entries
        """
        return iter(self._entries)
    
    def __contains__(self, entry: Entry) -> bool:
        """
        Check if an entry is contained in this directory.
        
        Args:
            entry (Entry): The entry to check for
            
        Returns:
            bool: True if the entry is in this directory
        """
        return entry in self._entries
    
    def __eq__(self, other) -> bool:
        """
        Check equality with another Directory.
        
        Args:
            other: Another object to compare with
            
        Returns:
            bool: True if directories have same name and contents
        """
        if not isinstance(other, Directory):
            return False
        return (self._name == other._name and 
                self._entries == other._entries)
    
    def __hash__(self) -> int:
        """
        Hash function for using Directory in sets and dictionaries.
        
        Returns:
            int: Hash value based on name
        """
        return hash(self._name)
