from typing import List
from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        c = Counter(nums)
        for _, v in c.items():
            if v % 2 != 0:
                return False
        return True