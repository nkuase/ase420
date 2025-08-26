"""
Memento Pattern - Gamer (Originator)
This class represents the originator that creates and restores mementos.
It maintains its state and can save/restore snapshots of that state.
"""

import random
from typing import List
from game.memento import Memento


class Gamer:
    """
    Gamer class that represents the originator in the Memento pattern.
    It can create mementos (snapshots) of its state and restore from them.
    """
    
    # Fruit names available in the game
    FRUIT_NAMES = ["apple", "grape", "banana", "orange"]
    
    def __init__(self, money: int):
        """
        Initialize the gamer with starting money.
        
        Args:
            money (int): Initial amount of money
        """
        self.money = money
        self.fruits: List[str] = []
        self.random = random.Random()
    
    def get_money(self) -> int:
        """
        Get the current amount of money.
        
        Returns:
            int: Current money amount
        """
        return self.money
    
    def bet(self):
        """
        Play the game by rolling a dice and applying the result.
        Different dice values have different effects on the game state.
        """
        dice = self.random.randint(1, 6)
        
        if dice == 1:
            # Roll 1: Money increases
            self.money += 100
            print("Your money increased!")
        elif dice == 2:
            # Roll 2: Money is halved
            self.money //= 2
            print("Your money was halved!")
        elif dice == 6:
            # Roll 6: Get a fruit
            fruit = self._get_fruit()
            print(f"You got a fruit: {fruit}")
            self.fruits.append(fruit)
        else:
            # Other rolls: Nothing happens
            print("Nothing happened.")
    
    def create_memento(self) -> Memento:
        """
        Create a memento (snapshot) of the current state.
        Only saves "delicious" fruits to demonstrate selective state saving.
        
        Returns:
            Memento: A memento containing the current state
        """
        memento = Memento(self.money)
        
        # Only save delicious fruits
        for fruit in self.fruits:
            if fruit.startswith("delicious "):
                memento.add_fruit(fruit)
        
        return memento
    
    def restore_memento(self, memento: Memento):
        """
        Restore the state from a memento.
        
        Args:
            memento (Memento): The memento to restore from
        """
        self.money = memento.get_money()
        self.fruits = memento.get_fruits()
    
    def _get_fruit(self) -> str:
        """
        Get a random fruit, with a 50% chance of it being "delicious".
        
        Returns:
            str: A fruit name, possibly prefixed with "delicious"
        """
        fruit = self.random.choice(self.FRUIT_NAMES)
        if self.random.choice([True, False]):
            return f"delicious {fruit}"
        else:
            return fruit
    
    def __str__(self) -> str:
        """
        String representation of the gamer's current state.
        
        Returns:
            str: String showing money and fruits
        """
        return f"[money = {self.money}, fruits = {self.fruits}]"
