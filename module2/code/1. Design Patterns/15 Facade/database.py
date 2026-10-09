class Database:
  
  def __init__(self):
    pass
  
  @staticmethod
  def get_properties(dbname):
    filename = f"{dbname}.txt"
    properties = {}
    
    try:
      with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
          line = line.strip()
          if line and '=' in line:
            key, value = line.split('=', 1)
            properties[key.strip()] = value.strip()
      return properties
    except IOError as e:
      raise IOError(f"Cannot read database file {filename}: {e}")
