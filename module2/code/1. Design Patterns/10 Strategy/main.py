"""
Simple Strategy Pattern Demo
============================
Shows how Strategy pattern works with Rock-Paper-Scissors.
No complex logic - just the core concept.
"""

from base_classes import Player
from rock_strategy import AlwaysRockStrategy
from paper_strategy import AlwaysPaperStrategy
from random_strategy import RandomStrategy


def main():
    print("Strategy Pattern Demo")
    print("=" * 30)
    
    # Create players with different strategies
    alice = Player("Alice", AlwaysRockStrategy())
    bob = Player("Bob", AlwaysPaperStrategy()) 
    charlie = Player("Charlie", RandomStrategy())
    
    players = [alice, bob, charlie]
    
    print("\nEach player uses a different strategy:")
    for player in players:
        print(f"  {player.name}: {player.get_strategy_name()}")
    
    print("\nLet's see what each player chooses:")
    for round in range(3):
        print(f"\nRound {round + 1}:")
        for player in players:
            hand = player.play()
            print(f"  {player.name} plays {hand}")
    
    print("\nNow let's switch Alice's strategy...")
    alice.set_strategy(RandomStrategy())
    print(f"Alice now uses: {alice.get_strategy_name()}")
    
    print(f"\nAlice's new choices:")
    for i in range(3):
        hand = alice.play() 
        print(f"  Alice plays {hand}")
    
if __name__ == "__main__":
    main()
