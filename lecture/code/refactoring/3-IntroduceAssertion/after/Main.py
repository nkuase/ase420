import random
from SortSample import SortSample

def execute(length: int):
    # Create random data
    data = [random.randint(0, length - 1) for _ in range(length)]
    
    # Display data
    sorter = SortSample(data)
    print(f"BEFORE:{sorter}")
    
    # Sort and display
    sorter.sort()
    print(f" AFTER:{sorter}")
    print()

def main():
    random.seed(1234)  # For reproducible results
    
    execute(10)
    execute(10)
    execute(10)
    execute(10)
    execute(10)

if __name__ == "__main__":
    main()
