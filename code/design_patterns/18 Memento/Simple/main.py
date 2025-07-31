import time
from game.gamer import Gamer
from game.memento import Memento


def main():
  
  print("=== Memento Pattern Demo ===\n")
  
  print("Starting the game with initial money: 100")
  print("Game rules:")
  print("- Roll 1: Money increases by 100")
  print("- Roll 2: Money is halved")
  print("- Roll 6: Get a fruit")
  print("- Other: Nothing happens")
  print("\nStrategy:")
  print("- Save state when money is more than memento")
  print("- Restore state when money drops to less than 1/2 amount of memento")
  
  gamer = Gamer(100) # $100 as a start
  memento = gamer.create_memento()
  
  print(f"\n{'='*60}")
  print("Game Progress:")
  print(f"{'='*60}")
  
  for i in range(30):
    print(f"\n==== Round {i + 1} ====")
    print(f"Current state: {gamer}")
    
    gamer.bet()
    
    current_money = gamer.get_money()
    saved_money = memento.get_money()
    
    print(f"Money is now: {current_money}")
    
    if current_money > saved_money:
      print("💾 Money increased significantly! Saving current state...")
      memento = gamer.create_memento()
    elif current_money < saved_money // 2:
      print("🔄 Money dropped too much! Restoring previous state...")
      gamer.restore_memento(memento)
    
    if gamer.get_money() <= 0:
      print("\n💀 Game Over! Money reached zero.")
      break
  
  print(f"\n{'='*60}")
  print("Game Statistics:")
  print(f"{'='*60}")
  print(f"Final state: {gamer}")
  print(f"Last saved state had: {memento.get_money()} money")


if __name__ == "__main__":
  main()
