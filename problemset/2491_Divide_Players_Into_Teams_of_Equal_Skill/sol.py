from typing import List
from collections import Counter
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        s = sum(skill)
        n = len(skill)
        if s % (n // 2) != 0:
            return -1
        avg_sum = s // (n // 2)
        
        count = Counter(skill)
        res = 0
        for x, cnt in count.items():
            if cnt == 0:
                continue
            y = avg_sum - x
            if y not in count or count[y] != cnt:
                return -1
            res += x * y * (cnt if x != y else cnt // 2)
            count[y] = 0
            
        return res
        