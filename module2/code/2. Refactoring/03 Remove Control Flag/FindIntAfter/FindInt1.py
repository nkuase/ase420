from typing import List

class FindInt:
    """Find integer in array using break (after refactoring step 1)"""
    
    @staticmethod
    def find(data: List[int], target: int) -> bool:
        found = False
        for i in range(len(data)):
            if data[i] == target:
                found = True
                break
        return found
