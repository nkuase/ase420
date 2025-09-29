from factory import Factory
from id_card import IDCard


class IDCardFactory(Factory):
  def part1(self):
    print('IDCardFactory part1')
  
  def part2(self):
    print('IDCardFactory part2')
    
  def create_product(self, owner): 
    self.part1()
    self.part2()
    print('create_product from IDCardFactory')
    return IDCard('create_product from IDCardFactory')
  