from support import Support
from trouble import Trouble


class SpecialSupport(Support):
  
  def __init__(self, name, number):
    super().__init__(name)
    self.number = number
  
  def resolve(self, trouble):
    return trouble.get_number() == self.number
