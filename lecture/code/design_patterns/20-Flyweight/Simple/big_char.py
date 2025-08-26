import os

class BigChar:
  def __init__(self, charname):
    self.charname = charname
    
    try:
      filename = f"big{charname}.txt"
      if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
          self.fontdata = f.read()
      else:
        self.fontdata = f"{charname}?\n"
    except IOError:
      self.fontdata = f"{charname}?\n"
  
  def print(self):
    print(self.fontdata, end='')
  
  def get_fontdata(self):
    return self.fontdata
  
  def __str__(self):
    return f"BigChar('{self.charname}')"
