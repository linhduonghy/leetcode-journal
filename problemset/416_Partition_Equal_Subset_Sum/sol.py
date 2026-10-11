from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        s = sum(nums)
        if s % 2 != 0:
            return False
        s //= 2
        n = len(nums)
        dp = [False] * (s + 1)
        dp[0] = True
        for i in range(n):
            for k in range(s, nums[i] - 1, -1):
                dp[k] = dp[k] or dp[k - nums[i]]
            if dp[s]:
                return True
        return False