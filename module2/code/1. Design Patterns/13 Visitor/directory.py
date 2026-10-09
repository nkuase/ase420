from entry import Entry
from visitor import Visitor


class Directory(Entry):
  
  def __init__(self, name):
    self.name = name
    self.directory = []
  
  def get_name(self):
    return self.name
  
  def get_size(self):
    total_size = 0
    for entry in self.directory:
      total_size += entry.get_size()
    return total_size
  
  def add(self, entry):
    self.directory.append(entry)
    return self
  
  def __iter__(self):
    return iter(self.directory)
  
  def accept(self, visitor):
    return visitor.visit_directory(self)
