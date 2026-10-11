from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
        nums.sort()        
        n = len(nums)
        i, j = 0, 0
        ans = 0
        print(nums)
        while i < n:
            while j < n and nums[j] - nums[i] <= 2 * k:
                j += 1
            ans = max(ans, j - i)
            if j == n:
                break
            i += 1
        
        return ans