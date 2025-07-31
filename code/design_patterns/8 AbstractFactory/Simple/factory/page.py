from factory.item import Item
from abc import ABC, abstractmethod


class Page(ABC):
  
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.content = []
  
  def add(self, item):
    self.content.append(item)
  
  def output(self, filename):
    try:
      with open(filename, 'w', encoding='utf-8') as f:
        f.write(self.make_html())
      print(f"File '{filename}' has been created.")
    except IOError as e:
      print(f"Error writing file: {e}")
  
  @abstractmethod
  def make_html(self):
    pass
