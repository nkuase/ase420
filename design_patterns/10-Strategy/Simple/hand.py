from enum import Enum


class Hand(Enum):
  
  ROCK = ("rock", 0)
  SCISSORS = ("scissors", 1) 
  PAPER = ("paper", 2)
  
  def __init__(self, label, hand_value):
    self.label = label
    self.hand_value = hand_value
  
  @classmethod
  def get_hand(cls, hand_value):
    hands = [cls.ROCK, cls.SCISSORS, cls.PAPER]
    if 0 <= hand_value <= 2:
      return hands[hand_value]
    else:
      raise ValueError(f"Invalid hand value: {hand_value}. Must be 0, 1, or 2.")
  
  def is_stronger_than(self, other):
    return self._fight(other) == 1
  
  def is_weaker_than(self, other):
    return self._fight(other) == -1
  
  def _fight(self, other):
    if self == other:
      return 0
    elif (self.hand_value + 1) % 3 == other.hand_value:
      return 1
    else:
      return -1
  
  def __str__(self):
    return self.label
  
  def __repr__(self):
    return f"Hand.{self.label}({self.label}, {self.hand_value})"


