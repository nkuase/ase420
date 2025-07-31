from support import Support
from trouble import Trouble


class LimitSupport(Support):
  
  def __init__(self, name, limit):
    super().__init__(name)
    self.limit = limit
  
  def resolve(self, trouble):
    return trouble.get_number() < self.limit
