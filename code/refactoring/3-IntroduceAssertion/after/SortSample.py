from typing import List

class SortSample:
    """Sorting example with assertions (after refactoring)"""
    
    def __init__(self, data: List[int]):
        self.data = data.copy()  # Create a copy
        
    def sort(self):
        """Selection sort implementation with assertions"""
        for x in range(len(self.data) - 1):
            m = x
            for y in range(x + 1, len(self.data)):
                if self.data[m] > self.data[y]:
                    m = y
            # Assert that data[m] is minimum in range [x, len(data)-1]
            assert self._is_min(m, x, len(self.data) - 1)
            
            v = self.data[m]
            self.data[m] = self.data[x]
            self.data[x] = v
            
            # Assert that data[0] to data[x+1] is sorted
            assert self._is_sorted(0, x + 1)
            
    def __str__(self):
        return "[ " + ", ".join(map(str, self.data)) + ", ]"
        
    def _is_min(self, pos: int, start: int, end: int) -> bool:
        """Check if data[pos] is minimum in range [start, end]"""
        for i in range(start, end + 1):
            if self.data[pos] > self.data[i]:
                return False
        return True
        
    def _is_sorted(self, start: int, end: int) -> bool:
        """Check if data[start] to data[end] is sorted"""
        for i in range(start, end):
            if self.data[i] > self.data[i + 1]:
                return False
        return True
