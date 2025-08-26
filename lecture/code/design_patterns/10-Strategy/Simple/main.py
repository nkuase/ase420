import sys
import time


from player import Player
from winning_strategy import WinningStrategy
from prob_strategy import ProbStrategy
from hand import Hand


def play_game(player1, player2, num_games = 10000, show_details = False):
  print(f"\nPlaying {num_games} games between {player1.get_name()} and {player2.get_name()}...")
  
  for i in range(num_games):
    hand1 = player1.next_hand()
    hand2 = player2.next_hand()
    
    if hand1.is_stronger_than(hand2):
      if show_details or i < 10:
        print(f"Game {i+1:4d}: {player1.get_name()}({hand1}) vs {player2.get_name()}({hand2}) - Winner: {player1.get_name()}")
      player1.win()
      player2.lose()
    elif hand2.is_stronger_than(hand1):
      if show_details or i < 10:
        print(f"Game {i+1:4d}: {player1.get_name()}({hand1}) vs {player2.get_name()}({hand2}) - Winner: {player2.get_name()}")
      player1.lose()
      player2.win()
    else:
      if show_details or i < 10:
        print(f"Game {i+1:4d}: {player1.get_name()}({hand1}) vs {player2.get_name()}({hand2}) - Tie")
      player1.even()
      player2.even()
  
  if num_games > 10:
    print("   ... (remaining games not shown)")


def analyze_strategies(player1, player2):
  print("\n" + "="*60)
  print("Strategy Analysis:")
  print("="*60)
  
  if isinstance(player1.get_strategy(), WinningStrategy):
    strategy = player1.get_strategy()
    print(f"\n{player1.get_name()}'s WinningStrategy:")
    print(f"  - Simple strategy: reuse winning hands")
    print(f"  - Current status: {strategy}")
  
  if isinstance(player2.get_strategy(), WinningStrategy):
    strategy = player2.get_strategy()
    print(f"\n{player2.get_name()}'s WinningStrategy:")
    print(f"  - Simple strategy: reuse winning hands")
    print(f"  - Current status: {strategy}")
  
  if isinstance(player1.get_strategy(), ProbStrategy):
    strategy = player1.get_strategy()
    print(f"\n{player1.get_name()}'s ProbStrategy:")
    print(f"  - Sophisticated strategy: learns from history")
    print(f"  - Current status: {strategy}")
    print(f"  - History matrix:")
    strategy.print_history()
  
  if isinstance(player2.get_strategy(), ProbStrategy):
    strategy = player2.get_strategy()
    print(f"\n{player2.get_name()}'s ProbStrategy:")
    print(f"  - Sophisticated strategy: learns from history")
    print(f"  - Current status: {strategy}")
    print(f"  - History matrix:")
    strategy.print_history()


def main():
  
  print("=== Strategy Pattern Example: Rock-Paper-Scissors ===")
  
  seed1 = int(time.time()) % 100          # Current time in seconds
  seed2 = int((time.time() * 1000) % 100)  # Milliseconds, modulo to keep it in a reasonable range
  
  print(f"Random seeds: {seed1}, {seed2}")
  
  player1 = Player("Sam", WinningStrategy(seed1))
  player2 = Player("John", ProbStrategy(seed2))
  
  print(f"\nPlayer 1: {player1.get_name()} using {type(player1.get_strategy()).__name__}")
  print(f"Player 2: {player2.get_name()} using {type(player2.get_strategy()).__name__}")
  
  play_game(player1, player2, 10000, show_details=False)
  
  print("\n" + "="*60)
  print("Final Results:")
  print("="*60)
  print(f"Total result:")
  print(player1)
  print(player2)
  
  print(f"\nDetailed Statistics:")
  print(player1.detailed_stats())
  print()
  print(player2.detailed_stats())
  print()
  
  analyze_strategies(player1, player2)


if __name__ == "__main__":
  main()
