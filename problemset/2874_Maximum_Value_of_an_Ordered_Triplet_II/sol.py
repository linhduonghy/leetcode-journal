from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        n = len(nums)
        imax = 0
        smax = 0
        ans = 0
        for k in range(n):
            ans = max(ans, smax * nums[k])
            smax = max(smax, imax - nums[k])
            imax = max(imax, nums[k])
        return ans