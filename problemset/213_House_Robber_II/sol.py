from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        max1 = dp[len(nums) - 2]

        dp = [0 for i in range(len(nums))]
        dp[1] = nums[1]
        dp[2] = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        return max(max1, dp[len(nums) - 1])