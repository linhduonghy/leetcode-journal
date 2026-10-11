from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        nums = nums + nums
        
        ans = [-1] * (2 * n)
        monotonic_stack = []
        
        for i, num in enumerate(nums):
            
            while monotonic_stack and nums[monotonic_stack[-1]] < num:
                ans[monotonic_stack.pop()] = num
            
            monotonic_stack.append(i)
        
        return ans[:n]