from strategy import Strategy
from hand import Hand


class Player:
  
  def __init__(self, name, strategy):
    self._name = name
    self._strategy = strategy
    self._win_count = 0
    self._lose_count = 0
    self._game_count = 0
  
  def next_hand(self):
    return self._strategy.next_hand()
  
  def win(self):
    self._strategy.study(True)
    self._win_count += 1
    self._game_count += 1
  
  def lose(self):
    self._strategy.study(False)
    self._lose_count += 1
    self._game_count += 1
  
  def even(self):
    self._game_count += 1
  
  def get_name(self):
    return self._name
  
  def get_strategy(self):
    return self._strategy
  
  def get_win_count(self):
    return self._win_count
  
  def get_lose_count(self):
    return self._lose_count
  
  def get_game_count(self):
    return self._game_count
  
  def get_tie_count(self):
    return self._game_count - self._win_count - self._lose_count
  
  def get_win_rate(self):
    if self._game_count == 0:
      return 0.0
    return (self._win_count / self._game_count) * 100.0
  
  def reset_stats(self):
    self._win_count = 0
    self._lose_count = 0
    self._game_count = 0
  
  def __str__(self):
    return (f"[{self._name}:"
            f"{self._game_count} games, "
            f"{self._win_count} win, "
            f"{self._lose_count} lose]")
  
  def detailed_stats(self):
    tie_count = self.get_tie_count()
    win_rate = self.get_win_rate()
    
    return (f"Player: {self._name}\n"
            f"  Total games: {self._game_count}\n"
            f"  Wins: {self._win_count}\n"
            f"  Losses: {self._lose_count}\n"
            f"  Ties: {tie_count}\n"
            f"  Win rate: {win_rate:.1f}%\n"
            f"  Strategy: {type(self._strategy).__name__}")
