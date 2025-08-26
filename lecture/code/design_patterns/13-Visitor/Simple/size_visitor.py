from visitor import Visitor
from file import File
from directory import Directory


class SizeVisitor(Visitor):
  
  def __init__(self):
    self.current_dir = ""
  
  def visit_file(self, file):
    print(f"{self.current_dir}/{file}")
    return file.size
  
  def visit_directory(self, directory):
    print(f"{self.current_dir}/{directory}")
    
    # Save current directory path
    saved_dir = self.current_dir
    self.current_dir = f"{self.current_dir}/{directory.get_name()}"
    
    # Calculate total size by visiting all entries in the directory
    total_size = 0
    for entry in directory:
      total_size += entry.accept(self)
    
    # Restore previous directory path
    self.current_dir = saved_dir
    
    return total_size
