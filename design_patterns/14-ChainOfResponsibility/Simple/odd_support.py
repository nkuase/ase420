from support import Support
from trouble import Trouble


class OddSupport(Support):
  
  def __init__(self, name):
    super().__init__(name)
  
  def resolve(self, trouble):
    return trouble.get_number() % 2 == 1
