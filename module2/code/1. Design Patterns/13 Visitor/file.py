from entry import Entry
from visitor import Visitor


class File(Entry):
  
  def __init__(self, name, size):
    self.name = name
    self.size = size
  
  def get_name(self):
    return self.name
  
  def get_size(self):
    return self.size
  
  def accept(self, visitor):
    return visitor.visit_file(self)
