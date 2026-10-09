from typing import List

class FindInt:
    """Find integer in array using early return (after refactoring step 2)"""
    
    @staticmethod
    def find(data: List[int], target: int) -> bool:
        for i in range(len(data)):
            if data[i] == target:
                return True
        return False
