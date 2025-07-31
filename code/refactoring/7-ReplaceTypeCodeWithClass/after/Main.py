from Item import Item
from ItemType import ItemType

def main():
    book = Item(
        ItemType.BOOK,
        "World History",
        4800)
    
    dvd = Item(
        ItemType.DVD,
        "New York Dreams Special Edition",
        3000)
    
    soft = Item(
        ItemType.SOFTWARE,
        "Turing Machine Emulator",
        3200)
    
    print(f"book = {book}")
    print(f"dvd  = {dvd}")
    print(f"soft = {soft}")

if __name__ == "__main__":
    main()
