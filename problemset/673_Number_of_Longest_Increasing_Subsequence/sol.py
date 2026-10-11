class Solution:
    """
        Sol O(n2):
            dp[i] = max(dp[j]) + 1 | j < i

        trace path with recursive
    """
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            maxPrev = 0
            for j in range(0, i):
                if nums[j] < nums[i] and maxPrev < dp[j]:
                    maxPrev = dp[j]
            dp[i] = maxPrev + 1

        count = 0
        m = max(dp)
        cache = [-1] * len(nums)
        cache[0] = 1
        for i in range(len(nums)):
            if dp[i] == m:
                count += self.dfs(dp, nums, i, cache)
        return count

    def dfs(self, dp: List[int], nums: List[int], index: int, cache: List[int]):
        if cache[index] != -1:
            return cache[index]
        count = 0
        for i in range(index):
            if nums[i] < nums[index] and dp[i] == dp[index] - 1:
                c = self.dfs(dp, nums, i, cache)
                cache[i] = c
                count += c
        return 1 if count == 0 else count