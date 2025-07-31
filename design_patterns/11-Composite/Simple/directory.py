from entry import Entry


class Directory(Entry):
  
  def __init__(self, name):
    self._name = name
    self._entries = []
  
  def get_name(self):
    return self._name
  
  def get_size(self):
    total_size = 0
    for entry in self._entries:
      total_size += entry.get_size()
    return total_size
  
  def _print_list(self, prefix):
    print(f"{prefix}/{self}")
    
    for entry in self._entries:
      entry._print_list(f"{prefix}/{self._name}")
  
  def add(self, entry):
    if not isinstance(entry, Entry):
      raise TypeError("Can only add Entry instances to directory")
    
    self._entries.append(entry)
    return self
  
  def remove(self, entry):
    try:
      self._entries.remove(entry)
      return True
    except ValueError:
      return False
  
  def remove_by_name(self, name):
    for entry in self._entries:
      if entry.get_name() == name:
        self._entries.remove(entry)
        return True
    return False
  
  def find(self, name):
    for entry in self._entries:
      if entry.get_name() == name:
        return entry
    return None
  
  def get_entries(self):
    return self._entries.copy()
  
  def get_files(self):
    from file import File
    return [entry for entry in self._entries if isinstance(entry, File)]
  
  def get_directories(self):
    return [entry for entry in self._entries if isinstance(entry, Directory)]
  
  def get_total_files(self):
    from file import File
    
    count = 0
    for entry in self._entries:
      if isinstance(entry, File):
        count += 1
      elif isinstance(entry, Directory):
        count += entry.get_total_files()
    return count
  
  def is_empty(self):
    return len(self._entries) == 0
  
  def __len__(self):
    return len(self._entries)
  
  def __iter__(self):
    return iter(self._entries)
  
  def __contains__(self, entry):
    return entry in self._entries
  
  def __eq__(self, other):
    if not isinstance(other, Directory):
      return False
    return (self._name == other._name and 
            self._entries == other._entries)
  
  def __hash__(self):
    return hash(self._name)
