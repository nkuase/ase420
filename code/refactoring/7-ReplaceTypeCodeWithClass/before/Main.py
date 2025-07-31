from Item import Item

def main():
    book = Item(
        Item.TYPECODE_BOOK,
        "World History",
        4800)
    
    dvd = Item(
        Item.TYPECODE_DVD,
        "New York Dreams Special Edition",
        3000)
    
    soft = Item(
        Item.TYPECODE_SOFTWARE,
        "Turing Machine Emulator",
        3200)
    
    print(f"book = {book}")
    print(f"dvd  = {dvd}")
    print(f"soft = {soft}")

if __name__ == "__main__":
    main()
