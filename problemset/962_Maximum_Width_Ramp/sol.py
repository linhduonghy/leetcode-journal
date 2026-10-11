from typing import List
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        nums = [(value, index) for index, value in enumerate(nums)]
        
        nums.sort(key=lambda x : (x[0], x[1]))
        n = len(nums)
        max_pos = nums[-1][1]
        res = 0
        for i in range(n - 1, -1, -1):
            res = max(res, max_pos - nums[i][1])
            max_pos = max(max_pos, nums[i][1])
            
        return res