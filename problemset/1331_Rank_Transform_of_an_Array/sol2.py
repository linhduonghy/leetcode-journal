from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        sorted_set = sorted(set(arr))
        ranks = {}
        for rank, v in enumerate(sorted_set):
            ranks[v] = rank + 1
        arr = [ranks[x] for x in arr]
                    
        return arr