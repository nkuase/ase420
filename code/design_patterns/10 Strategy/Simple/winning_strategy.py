import random
from strategy import Strategy
from hand import Hand


class WinningStrategy(Strategy):
  
  def __init__(self, seed):
    self._random = random.Random(seed)
    self._won = False
    self._prev_hand = None
  
  def next_hand(self):
    if not self._won:
      self._prev_hand = Hand.get_hand(self._random.randint(0, 2))
    
    return self._prev_hand
  
  def study(self, win):
    self._won = win
  
  def get_win_status(self):
    return self._won
  
  def get_previous_hand(self):
    return self._prev_hand
  
  def __str__(self):
    return f"WinningStrategy(won_last={self._won}, prev_hand={self._prev_hand})"
