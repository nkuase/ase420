from entry import Entry


class File(Entry):
  
  def __init__(self, name, size):
    if size < 0:
      raise ValueError("File size cannot be negative")
    
    self._name = name
    self._size = size
  
  def get_name(self):
    return self._name
  
  def get_size(self):
    return self._size
  
  def _print_list(self, prefix):
    print(f"{prefix}/{self}")
  
  def set_size(self, size):
    if size < 0:
      raise ValueError("File size cannot be negative")
    self._size = size
  
  def get_extension(self):
    if '.' in self._name:
      return self._name.split('.')[-1]
    return ""
  
  def get_basename(self):
    if '.' in self._name:
      return '.'.join(self._name.split('.')[:-1])
    return self._name
  
  def __eq__(self, other):
    if not isinstance(other, File):
      return False
    return self._name == other._name and self._size == other._size
  
  def __lt__(self, other):
    if not isinstance(other, File):
      return NotImplemented
    return self._name < other._name
  
  def __hash__(self):
    return hash((self._name, self._size))
