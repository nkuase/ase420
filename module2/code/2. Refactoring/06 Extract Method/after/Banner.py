class Banner:
    """Banner class with extracted methods (after refactoring)"""
    
    def __init__(self, content):
        self.content = content
        
    def print_banner(self, times):
        self._print_border()
        self._print_content(times)
        self._print_border()
        
    def _print_border(self):
        """Extracted method for printing border"""
        print("+", end="")
        for i in range(len(self.content)):
            print("-", end="")
        print("+")
        
    def _print_content(self, times):
        """Extracted method for printing content"""
        for i in range(times):
            print(f"|{self.content}|")
