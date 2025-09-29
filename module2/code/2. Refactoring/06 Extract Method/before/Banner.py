class Banner:
    """Banner class with duplicate code (before refactoring)"""
    
    def __init__(self, content):
        self.content = content
        
    def print_banner(self, times):
        # Print top border
        print("+", end="")
        for i in range(len(self.content)):
            print("-", end="")
        print("+")
        
        # Print content
        for i in range(times):
            print(f"|{self.content}|")
            
        # Print bottom border (duplicate code)
        print("+", end="")
        for i in range(len(self.content)):
            print("-", end="")
        print("+")
