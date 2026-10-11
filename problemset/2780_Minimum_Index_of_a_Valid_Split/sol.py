from typing import List
from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
    
        counter = Counter(nums)
        dominant = counter.most_common(1)[0]
        
        c = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == dominant[0]:
                c += 1
            if c * 2 > i + 1 and dominant[1] * 2 > n - i:
                return i
                
        return -1