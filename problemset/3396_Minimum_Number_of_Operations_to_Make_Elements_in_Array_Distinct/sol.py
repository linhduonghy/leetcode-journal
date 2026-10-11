from typing import List
import math
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
    
        n = len(nums)
        s = set()
        s.add(nums[-1])
        for i in range(n - 2, -1, -1):
            if nums[i] in s:
                return math.ceil((i + 1) / 3)
            s.add(nums[i])
        return 0