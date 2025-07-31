import threading
from big_char import BigChar

class BigCharFactory:
  _instance = None
  _lock = threading.Lock()
  
  def __new__(cls):
    if cls._instance is None:
      with cls._lock:
        if cls._instance is None:
          cls._instance = super().__new__(cls)
          cls._instance._pool = {}
    return cls._instance
  
  @classmethod
  def get_instance(cls):
    if cls._instance is None:
      cls._instance = cls()
    return cls._instance
  
  def get_big_char(self, charname):
    with self._lock:
      if charname not in self._pool:
        print(f"Creating new BigChar for '{charname}'")
        self._pool[charname] = BigChar(charname)
      else:
        print(f"Reusing existing BigChar for '{charname}'")
      
      return self._pool[charname]
  
  def get_pool_size(self):
    return len(self._pool)
  
  def get_cached_characters(self):
    return list(self._pool.keys())
  
  def clear_pool(self):
    with self._lock:
      self._pool.clear()
      print("Flyweight pool cleared")
