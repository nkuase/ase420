"""
Memento Pattern Demo
This example demonstrates the Memento pattern through a simple game
where a player can save and restore their game state.

Key concepts demonstrated:
1. Capturing and storing object state without violating encapsulation
2. Providing rollback functionality
3. Narrow and wide interfaces for different access levels
4. Originator creates and restores from mementos
"""

import time
from game.gamer import Gamer
from game.memento import Memento


def main():
    """
    Main function that demonstrates the Memento pattern.
    Simulates a game where the player's state can be saved and restored.
    """
    print("=== Memento Pattern Demo ===\n")
    
    print("Starting the game with initial money: 100")
    print("Game rules:")
    print("- Roll 1: Money increases by 100")
    print("- Roll 2: Money is halved")
    print("- Roll 6: Get a fruit")
    print("- Other: Nothing happens")
    print("\nStrategy:")
    print("- Save state when money increases significantly")
    print("- Restore state when money drops to less than half of saved amount")
    print("- Only 'delicious' fruits are saved in mementos")
    
    # Initialize the game
    gamer = Gamer(100)
    memento = gamer.create_memento()  # Save initial state
    
    print(f"\n{'='*60}")
    print("Game Progress:")
    print(f"{'='*60}")
    
    # Game loop
    for i in range(100):
        print(f"\n==== Round {i + 1} ====")
        print(f"Current state: {gamer}")
        
        # Play one round
        gamer.bet()
        
        current_money = gamer.get_money()
        saved_money = memento.get_money()
        
        print(f"Money is now: {current_money}")
        
        # Memento management strategy
        if current_money > saved_money:
            print("💾 Money increased significantly! Saving current state...")
            memento = gamer.create_memento()
        elif current_money < saved_money // 2:
            print("🔄 Money dropped too much! Restoring previous state...")
            gamer.restore_memento(memento)
        
        # Short pause for readability
        time.sleep(0.5)
        
        # Stop if money reaches zero
        if gamer.get_money() <= 0:
            print("\n💀 Game Over! Money reached zero.")
            break
    
    print(f"\n{'='*60}")
    print("Game Statistics:")
    print(f"{'='*60}")
    print(f"Final state: {gamer}")
    print(f"Last saved state had: {memento.get_money()} money")
    
    print("\nMemento Pattern Benefits Demonstrated:")
    print("1. ✅ State Encapsulation: Internal state is saved without exposing implementation")
    print("2. ✅ Selective Saving: Only 'delicious' fruits are saved, demonstrating selective state capture")
    print("3. ✅ Rollback Capability: Game state can be restored to previous good states")
    print("4. ✅ Multiple Save Points: Could easily extend to support multiple mementos")
    
    print("\nKey Points:")
    print("- Memento captures object state without violating encapsulation")
    print("- Originator (Gamer) creates and restores from mementos")
    print("- Caretaker (Main) stores mementos but doesn't access their contents")
    print("- Narrow interface limits caretaker access to memento internals")
    print("- Wide interface allows originator full access to memento state")
    print("- Useful for undo/redo functionality, checkpoints, and state management")


if __name__ == "__main__":
    main()
