import random
from game.memento import Memento


class Gamer:
  
  FRUIT_NAMES = ["apple", "grape", "banana", "orange"]
  
  def __init__(self, money):
    self.money = money
    self.fruits = []
    self.random = random.Random()
  
  def get_money(self):
    return self.money
  
  def bet(self):
    dice = self.random.randint(1, 6)
    
    if dice == 1:
      self.money += 100
      print("Your money increased!")
    elif dice == 2:
      self.money //= 2
      print("Your money was halved!")
    elif dice == 6:
      fruit = self._get_fruit()
      print(f"You got a fruit: {fruit}")
      self.fruits.append(fruit)
    else:
      print("Nothing happened.")
  
  def create_memento(self):
    memento = Memento(self.money)
    
    for fruit in self.fruits:
      memento.add_fruit(fruit)
    
    return memento
  
  def restore_memento(self, memento):
    self.money = memento.get_money()
    self.fruits = memento.get_fruits()
  
  def _get_fruit(self):
    fruit = self.random.choice(self.FRUIT_NAMES)
    return fruit
  
  def __str__(self):
    return f"[money = {self.money}, fruits = {self.fruits}]"
