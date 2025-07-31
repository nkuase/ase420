from Dice import Dice

def main():
    dice0 = Dice()
    dice1 = Dice(456)
    dice2 = Dice()
    dices = [dice0, dice1, dice2]
    
    dice2.seed(456)  # Reset seed
    
    for dice in dices:
        for i in range(10):
            print(f"{dice.next_int()}, ", end="")
        print()

if __name__ == "__main__":
    main()
