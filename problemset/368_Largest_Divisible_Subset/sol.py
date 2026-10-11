from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        dp = [0 for _ in range(n)]
        prev = [-1 for _ in range(n)]
        max_len = 0
        i_max = -1
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = max(dp[i], dp[j] + 1)
                    prev[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                i_max = i
        result = []
        i = i_max
        while i != -1:
            result.append(nums[i])
            i = prev[i]
        return result