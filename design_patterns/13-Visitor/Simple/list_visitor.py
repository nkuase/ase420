from visitor import Visitor
from file import File
from directory import Directory


class ListVisitor(Visitor):
  
  def __init__(self):
    self.current_dir = ""
  
  def visit_file(self, file):
    print(f"{self.current_dir}/{file}")
  
  def visit_directory(self, directory):
    print(f"{self.current_dir}/{directory}")
    
    saved_dir = self.current_dir
    
    self.current_dir = f"{self.current_dir}/{directory.get_name()}"
    
    for entry in directory:
      entry.accept(self)
    
    self.current_dir = saved_dir
