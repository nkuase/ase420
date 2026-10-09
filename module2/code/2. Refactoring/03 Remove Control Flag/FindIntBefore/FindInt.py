from typing import List

class FindInt:
    """Find integer in array using control flag (before refactoring)"""
    
    @staticmethod
    def find(data: List[int], target: int) -> bool:
        flag = False
        i = 0
        while i < len(data) and not flag:
            if data[i] == target:
                flag = True
            i += 1
        return flag
