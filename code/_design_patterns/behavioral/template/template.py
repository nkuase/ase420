# Interfaces
class AbstractBuild(object):
  def build_roof(self):
    print("Building roof")
  def build_walls(self):
    print("Building walls")
  def build_chimney(self):
    print("Building chimney")
  def build_basement(self):
    print("Building basement")

# Implementations    
class HouseBuild(AbstractBuild):
  def design_house(self):
    print("Design before building")
  def build(self):
    self.design_house()
    self.build_basement()
    self.build_walls()
    self.build_roof()
    self.build_chimney()
    
class SmallHouseBuild(AbstractBuild):  
  def build_walls(self):
    print(">>> Build small walls")  
  def build(self):
    self.build_walls()
    self.build_roof()

# Driver    
b = HouseBuild()
b.build()

print("<Building a small house>")
s = SmallHouseBuild()
s.build()