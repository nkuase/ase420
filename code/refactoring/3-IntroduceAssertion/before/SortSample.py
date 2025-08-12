from typing import List

class SortSample:
    """Sorting example without assertions (before refactoring)"""
    
    def __init__(self, data: List[int]):
        self.data = data.copy()  # Create a copy
        
    def sort(self):
        """Selection sort implementation"""
        for x in range(len(self.data) - 1):
            m = x
            for y in range(x + 1, len(self.data)):
                if self.data[m] > self.data[y]:
                    m = y
            # Here data[m] should be the minimum of data[x] ~ data[len(data)-1]
            v = self.data[m]
            self.data[m] = self.data[x]
            self.data[x] = v
            # Here data[0] ~ data[x+1] should already be sorted
            
    def __str__(self):
        return "[ " + ", ".join(map(str, self.data)) + ", ]"
