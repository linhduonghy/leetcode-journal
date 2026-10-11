from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        res = float("-inf")
        sum = nums[0]
        min_v = nums[0]
        max_v = nums[0]
        for i in range(1, len(nums)):
            sum += nums[i]
            res = max(res, abs(sum), abs(sum - min_v), abs(sum - max_v))
            min_v = min(min_v, sum)
            max_v = max(max_v, sum)
            
        return res