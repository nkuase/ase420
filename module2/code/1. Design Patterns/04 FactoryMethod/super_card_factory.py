from factory import Factory
from super_card import SuperCard


class SuperCardFactory(Factory):
  def part1(self):
    print('SuperCardFactory part1')
  
  def part2(self):
    print('SuperCardFactory part2')
    
  def create_product(self, owner):
    self.part1()
    self.part2()
    print('create_product from SuperCardFactory')
    return SuperCard(owner)