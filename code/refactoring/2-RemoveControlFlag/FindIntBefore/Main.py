from FindInt import FindInt

def main():
    data = [1, 9, 0, 2, 8, 5, 6, 3, 4, 7]
    
    if FindInt.find(data, 5):
        print("Found!")
    else:
        print("Not found...")

if __name__ == "__main__":
    main()
