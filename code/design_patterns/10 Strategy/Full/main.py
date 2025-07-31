"""
Main module for Strategy Pattern Example

This demonstrates the Strategy pattern through a Rock-Paper-Scissors game
where two players use different strategies. The Strategy pattern allows
the algorithm (strategy) to be selected and changed at runtime.

Key concepts demonstrated:
1. Strategy interface - defines common interface for all strategies
2. Concrete Strategies - WinningStrategy and ProbStrategy with different algorithms
3. Context (Player) - uses strategies without knowing their implementation details
4. Runtime strategy selection - different players can use different strategies

Usage:
    python main.py <seed1> <seed2>
    
Example:
    python main.py 314 15
"""

import sys
from player import Player
from winning_strategy import WinningStrategy
from prob_strategy import ProbStrategy
from hand import Hand


def play_game(player1: Player, player2: Player, num_games: int = 10000, 
              show_details: bool = False) -> None:
    """
    Play a series of Rock-Paper-Scissors games between two players.
    
    Args:
        player1 (Player): First player
        player2 (Player): Second player
        num_games (int): Number of games to play
        show_details (bool): Whether to show each game result
    """
    print(f"\nPlaying {num_games} games between {player1.get_name()} and {player2.get_name()}...")
    
    for i in range(num_games):
        # Each player makes their move
        hand1 = player1.next_hand()
        hand2 = player2.next_hand()
        
        # Determine winner and update scores
        if hand1.is_stronger_than(hand2):
            if show_details or i < 10:  # Show first 10 games for demonstration
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


def analyze_strategies(player1: Player, player2: Player) -> None:
    """
    Analyze and display information about the strategies used.
    
    Args:
        player1 (Player): First player
        player2 (Player): Second player
    """
    print("\n" + "="*60)
    print("Strategy Analysis:")
    print("="*60)
    
    # Analyze WinningStrategy
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
    
    # Analyze ProbStrategy
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
    """Main function demonstrating the Strategy pattern."""
    
    print("=== Strategy Pattern Example: Rock-Paper-Scissors ===")
    
    # Parse command line arguments (similar to Java version)
    if len(sys.argv) != 3:
        print("\nUsage: python main.py randomseed1 randomseed2")
        print("Example: python main.py 314 15")
        print("\nUsing default seeds 314 and 15...")
        seed1, seed2 = 314, 15
    else:
        try:
            seed1 = int(sys.argv[1])
            seed2 = int(sys.argv[2])
        except ValueError:
            print("Error: Seeds must be integers")
            print("Using default seeds 314 and 15...")
            seed1, seed2 = 314, 15
    
    print(f"Random seeds: {seed1}, {seed2}")
    
    # Create players with different strategies
    player1 = Player("KIM", WinningStrategy(seed1))
    player2 = Player("LEE", ProbStrategy(seed2))
    
    print(f"\nPlayer 1: {player1.get_name()} using {type(player1.get_strategy()).__name__}")
    print(f"Player 2: {player2.get_name()} using {type(player2.get_strategy()).__name__}")
    
    # Play games
    play_game(player1, player2, 10000, show_details=False)
    
    # Show final results
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
    
    # Analyze strategies
    analyze_strategies(player1, player2)
    
    # Demonstrate strategy pattern benefits
    print("\n" + "="*60)
    print("Strategy Pattern Benefits Demonstrated:")
    print("="*60)
    
    print("\n1. Algorithm Encapsulation:")
    print("   - Each strategy encapsulates a different algorithm")
    print("   - WinningStrategy: Simple reuse of winning moves")
    print("   - ProbStrategy: Complex probabilistic learning")
    
    print("\n2. Runtime Strategy Selection:")
    print("   - Players can use different strategies")
    print("   - Strategies can be changed without modifying Player class")
    
    print("\n3. Strategy Independence:")
    print("   - Players don't know strategy implementation details")
    print("   - Strategies can evolve independently")
    
    print("\n4. Easy Extensibility:")
    print("   - New strategies can be added easily")
    print("   - No modification of existing code required")
    
    # Demonstrate strategy swapping
    print(f"\n5. Strategy Swapping Demo:")
    print("   Creating new players with swapped strategies...")
    
    player3 = Player("PARK", ProbStrategy(seed1))
    player4 = Player("CHOI", WinningStrategy(seed2))
    
    print(f"   {player3.get_name()} now uses ProbStrategy")
    print(f"   {player4.get_name()} now uses WinningStrategy")
    
    play_game(player3, player4, 100, show_details=False)
    print(f"   Results after 100 games:")
    print(f"   {player3}")
    print(f"   {player4}")


if __name__ == "__main__":
    main()
