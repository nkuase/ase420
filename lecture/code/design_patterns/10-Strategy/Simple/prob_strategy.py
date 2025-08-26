import random
from strategy import Strategy
from hand import Hand


class ProbStrategy(Strategy):
  
  def __init__(self, seed):
    self._random = random.Random(seed)
    self._prev_hand_value = 0
    self._current_hand_value = 0
    
    self._history = [
      [1, 1, 1],
      [1, 1, 1], 
      [1, 1, 1]
    ]
  
  def next_hand(self):
    bet = self._random.randint(0, self._get_sum(self._current_hand_value) - 1)
    
    hand_value = 0
    if bet < self._history[self._current_hand_value][0]:
      hand_value = 0
    elif bet < (self._history[self._current_hand_value][0] + 
               self._history[self._current_hand_value][1]):
      hand_value = 1
    else:
      hand_value = 2
    
    self._prev_hand_value = self._current_hand_value
    self._current_hand_value = hand_value
    
    return Hand.get_hand(hand_value)
  
  def _get_sum(self, hand_value):
    return sum(self._history[hand_value])
  
  def study(self, win):
    if win:
      self._history[self._prev_hand_value][self._current_hand_value] += 1
    else:
      self._history[self._prev_hand_value][(self._current_hand_value + 1) % 3] += 1
      self._history[self._prev_hand_value][(self._current_hand_value + 2) % 3] += 1
  
  def get_history_matrix(self):
    return [row[:] for row in self._history]
  
  def get_probabilities(self, hand_value):
    total = self._get_sum(hand_value)
    return [freq / total for freq in self._history[hand_value]]
  
  def __str__(self):
    return f"ProbStrategy(prev={self._prev_hand_value}, current={self._current_hand_value})"
  
  def print_history(self):
    print("History Matrix (frequency of hand transitions):")
    print("    From\\To  Rock  Scissors  Paper")
    hand_names = ["Rock    ", "Scissors", "Paper   "]
    for i, row in enumerate(self._history):
      print(f"    {hand_names[i]}  {row[0]:4d}  {row[1]:8d}  {row[2]:5d}")
